import subprocess # コマンド実行ライブラリ
import RPi.GPIO as GPIO # RPi.GPIOモジュールを使用
import time # timeライブラリ
import os

# ソースファイルの場所取得
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# GPIOの使用するピン番号
gpio_sw = 21
# GPIO番号指定の準備
GPIO.setmode(GPIO.BCM)
# スイッチピンを入力、プルアップに設定
GPIO.setup(gpio_sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Node-REDの起動コマンドを実行（同期処理）
nodered_start_cmd = 'node-red-pi --max-old-space-size=256'
nodered_prop = subprocess.Popen("exec " + nodered_start_cmd, shell=True)
time.sleep(9)

# 永久ループでGPIOをの状態をチェックする
while True :
    # スイッチの状態を取得
    sw_1 = GPIO.input(gpio_sw)
    # 物が置いてなかったら
    if sw_1 == 1 :
        chromium_cmd = 'chromium-browser --noerrdialogs --kiosk http://localhost:1880/clock'
        clock_prop = subprocess.Popen("exec " + chromium_cmd, shell=True)
        time.sleep(0.1)
        while True :
            time.sleep(0.1)
            # スイッチの状態を取得
            sw_2 = GPIO.input(gpio_sw)
            if sw_2 == 0 :
                clock_prop.kill()
                time.sleep(0.1)
                break
    elif sw_1 == 0:
        while True :
            time.sleep(0.1)
            # スイッチの状態を取得
            sw_2 = GPIO.input(gpio_sw)
            if sw_2 == 1 :
                time.sleep(5)
                sw_3 = GPIO.input(gpio_sw)
                if sw_3 == 1 :
                    # ここでファイル読み込みする
                    status = '0'
                    if os.path.exists(APP_ROOT+'/talkStatus.txt') :
                        with open(APP_ROOT+'/talkStatus.txt', 'r') as f:
                            status = f.readline()
                    
                    chromium_cmd = 'chromium-browser --noerrdialogs --kiosk https://meijoryoga.mybluemix.net/video-chat?status=' + status 
                    videochat_prop = subprocess.Popen("exec " + chromium_cmd, shell=True)
                    python_cmd = 'python3 /home/pi/HackAichi2020/src/makeConversationLevel.py'
                    python_prop = subprocess.Popen("exec " + python_cmd, shell=True)
                    for i in range(0, 20):
                        sw_4 = GPIO.input(gpio_sw)
                        if sw_4 == 0 :
                            break
                        else:
                            time.sleep(1)
                    videochat_prop.kill()
                    break