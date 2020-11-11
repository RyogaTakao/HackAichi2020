import subprocess # コマンド実行ライブラリ
import RPi.GPIO as GPIO # RPi.GPIOモジュールを使用
import time # timeライブラリ

# GPIOの使用するピン番号
gpio_sw = 21
# GPIO番号指定の準備
GPIO.setmode(GPIO.BCM)
# スイッチピンを入力、プルアップに設定
GPIO.setup(gpio_sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)

clock_prop = object
video_prop = object

before_sw = 1

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
chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk --incognito http://localhost:1880/home'
prop_clock = run_cmd_func(chromium_start_cmd, 'async')

# 永久ループでGPIOをの状態をチェックする
while True :
    # スイッチの状態を取得
    sw = GPIO.input(gpio_sw)
    if before_sw != sw :
        if sw == 0 : # ものが置かれている
            time.sleep(5)
            sw = GPIO.input(gpio_sw)
            if sw == 0 : # まだものが置かれているなら 背景にする
                if clock_prop : # 時計が表示されていたら消す
                    clock_prop.kill()
                    clock_prop = ''
                if video_prop : # ビデオが表示されていたら消す
                    video_prop.kill()
                    clock_prop = ''
            else : 
                chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk --incognito http://localhost:1880/videochat'
                video_prop = run_cmd_func(chromium_start_cmd, 'async')
                if clock_prop : # 時計が表示されていたら消す
                    clock_prop.kill()
                    clock_prop = ''
                time.sleep(330)
                before_sw = sw
        else : # ものが置かれていない
            time.sleep(5)
            sw = GPIO.input(gpio_sw)
            if sw == 1 : # ものが置かれていない
                chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk --incognito http://localhost:1880/clock'
                clock_prop = run_cmd_func(chromium_start_cmd, 'async')
                if video_prop : # ビデオチャットが表示されていたら消す
                    video_prop.kill()
                    video_prop = ''
                before_sw = sw


