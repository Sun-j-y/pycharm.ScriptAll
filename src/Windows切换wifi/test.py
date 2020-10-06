import os
import subprocess

import time


# 百度ip
ipTest = '61.135.169.121'
# 可以切换的wifi
wifiList = ['Tenda_D05B41', 'Tenda_D05B40', 'Tenda_D05B42']

cmd = 'netsh wlan show interfaces'
p = subprocess.Popen(cmd,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=True)
print(p)
ret = p.stdout.read()
print(ret)
index = ret.decode(encoding='unicode_escape').split(':')

t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


"""
while True:
    current_wifi = get_current_wifi()
    print("当前的wifi为：", current_wifi)
    if check_ping(ipTest, 2) != 'ok':
        print("联网失败，正在切换wifi")
        if auto_switch_wifi(wifiList) == 'ok':
            print("切换成功")
            print("-" * 40)
        else:
            continue
        time.sleep(5)
    else:
        print("可以成功联网")
        print('-' * 40)
        time.sleep(5)
        
cmd = 'netsh wlan connect name={}'.format("Tenda_D05B42")
os.system(cmd)
"""
