import subprocess

# juliusデモの立ち上げ
subprocess.run(['sudo', 'modprobe', 'snd-pcm-oss'])
proc_julius = subprocess.run(['julius', '-C', '/home/pi/dictation-kit-v4.3.1-linux/main.jconf', '-C', '/home/pi/dictation-kit-v4.3.1-linux/am-gmm.jconf', '-demo'])