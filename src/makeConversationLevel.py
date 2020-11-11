import socket
import subprocess
import time

# juliusローカルサーバの立ち上げ
proc_julius = subprocess.Popen(['julius', '-C', 'main.jconf', '-C', 'am-dnn.jconf', '-module', '-charconv', 'utf-8', 'sjis', '-dnnconf', 'julius.dnnconf'])
time.sleep(10)

# Juliusにソケット通信で接続
client_julius = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_julius.connect(('localhost', 10500))

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
            data =""
        else:
            data += str(client_julius.recv(1024).decode('utf-8'))
            print('NotFound')
except KeyboardInterrupt:
    print('finished')
    client_julius.send("DIE".encode('utf-8'))
    client_julius.close()
    proc_julius.kill()