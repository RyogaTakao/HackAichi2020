import subprocess # コマンド実行ライブラリ
import RPi.GPIO as GPIO # RPi.GPIOモジュールを使用
import time # timeライブラリ

# GPIOの使用するピン番号
gpio_sw = 21
# GPIO番号指定の準備
GPIO.setmode(GPIO.BCM)
# スイッチピンを入力、プルアップに設定
GPIO.setup(gpio_sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# コマンド実行関数
# async :非期処理 sync :同期処理
def run_cmd_func (cmd , status) :
    
    run_cmd = cmd.split()
    if status == 'sync' :
        subprocess.run(run_cmd)
    elif status == 'async':
        log = subprocess.Popen(run_cmd)
        return log
    else:
        print('status error decide sync or async')

# 実行フローはここから========================================

# Node-REDの起動コマンドを実行（同期処理）
# nodered_start_cmd = 'node-red-pi --max-old-space-size=256'
# run_cmd_func(nodered_start_cmd, 'sync')

# 背景をkioskモードで表示するコマンドを実行
chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk http://localhost:1880/home'
run_cmd_func(chromium_start_cmd, 'async')

# 永久ループでGPIOをの状態をチェックする
while True :
    # スイッチの状態を取得
    sw_1 = GPIO.input(gpio_sw)
    # 物が置いてなかったら
    if sw_1 == 1 :
        chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk http://localhost:1880/clock'
        run_cmd_func(chromium_start_cmd, 'async')
        print('clock')
        while True :
            time.sleep(0.1)
            # スイッチの状態を取得
            sw_2 = GPIO.input(gpio_sw)
            if sw_2 == 0 :
                chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk http://localhost:1880/home'
                run_cmd_func(chromium_start_cmd, 'async')
                print('home')
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
                    chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk http://localhost:1880/videochat'
                    run_cmd_func(chromium_start_cmd, 'async')
                    print('video')
                    for i in range(0, 300):
                        sw_4 = GPIO.input(gpio_sw)
                        if sw_4 == 0 :
                            chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk http://localhost:1880/home'
                            run_cmd_func(chromium_start_cmd, 'async')
                            break
                        else:
                            time.sleep(1)
                    break