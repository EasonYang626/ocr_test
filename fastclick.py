import os, time
import _thread
# for i in range(0, 20):
# 	os.system('adb shell input tap 500 500')
# 	time.sleep(1)
def shell(sql):
    os.system(sql)
while True:
    _thread.start_new_thread(shell,('adb shell input tap 978 1814',))
    # os.system('adb shell input tap 978 1814')
    time.sleep(0.15)