import subprocess # コマンド実行ライブラリ
import RPi.GPIO as GPIO # RPi.GPIOモジュールを使用
import time # timeライブラリ

# GPIOの使用するピン番号
gpio_sw = 40
# GPIO番号指定の準備
GPIO.setmode(GPIO.BCM)
# スイッチピンを入力、プルアップに設定
GPIO.setup(gpio_sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIOの状態に変化が生じたことを確認する変数
gpio_after = 0

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
nodered_start_cmd = 'node-red-pi --max-old-space-size=256'
run_cmd_func(nodered_start_cmd, 'sync')

# スタート画面（時計）をkioskモードで表示するコマンドを実行
chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk --incognito http://localhost:1880/clock'
prop_clock = run_cmd_func(chromium_start_cmd, 'async')

# 永久ループでGPIOをの状態をチェックする
while True :
    # スイッチの状態を取得
    sw = GPIO.input(gpio_sw)
    # スイッチの状態に変化が存在していれば処理を開始
    if (gpio_after != sw) :
        # スイッチが押されていたら（ON = 0）
        if sw == 0 :
            # コマンドラインでSkyWayを起動するページを表示する処理を追加
            chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk --incognito http://localhost:1880/videochat'
            prop_skyway = run_cmd_func(chromium_start_cmd, 'async')
            # clockを消す
            prop_clock.kill()
            #gpioの最終状態を保存
            gpio_after = sw
        # スイッチが押されていなかったら
        else :
            # コマンドラインで時計ページを表示する処理を追加
            chromium_start_cmd = 'chromium-browser --noerrdialogs --kiosk --incognito http://localhost:1880/clock'
            prop_skyway = run_cmd_func(chromium_start_cmd, 'async')
            # clockを消す
            prop_clock.kill()
            #gpioの最終状態を保存
            gpio_after = sw
