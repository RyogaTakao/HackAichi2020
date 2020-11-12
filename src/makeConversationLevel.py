import os
import socket
import subprocess
import time

# ソースファイルの場所取得
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# juliusローカルサーバの立ち上げ
subprocess.run(['sudo', 'modprobe', 'snd-pcm-oss'])
proc_julius = subprocess.Popen(['julius', '-C', '/home/pi/dictation-kit-v4.3.1-linux/main.jconf', '-C', '/home/pi/dictation-kit-v4.3.1-linux/am-gmm.jconf', '-module'])
time.sleep(5)

# Juliusにソケット通信で接続
client_julius = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_julius.connect(('localhost', 10500))

arry_word = []

try:
    data = ""
    while True:
        if '</RECOGOUT>\n.' in data:
            # 出力結果から認識した単語を取り出す
            recog_text = ""
            for line in data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"', index+6)]
                    recog_text = recog_text + line
            print("認識結果: " + recog_text)
            arry_word.append(recog_text)
            data =""
        else:
            data += str(client_julius.recv(1024).decode('utf-8'))
            print('NotFound')
except KeyboardInterrupt:
    talk_status = 0
    print('finished')
    print(arry_word)
    client_julius.send("DIE".encode('utf-8'))
    client_julius.close()
    proc_julius.kill()
    if len(arry_word) > 10:
        talk_status = 2
    elif 5 < len(arry_word) < 10:
        talk_status = 1
    # トークステータスをテキストファイルに保存
    with open(APP_ROOT+'/talkStatus.txt', 'w') as f:
        print(talk_status, file=f)
        print('', file=f)
        for word in arry_word:
            print(word, file=f)