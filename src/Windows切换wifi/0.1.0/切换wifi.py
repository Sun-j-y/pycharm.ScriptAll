"""
Windows自动切换WiFi v0.1.0
    原始代码来自于: https://blog.csdn.net/qq_34377830/article/details/82497457
    此版本已经做了大量更改
"""
import os
import subprocess
import random
import time

# 百度ip
ipTest = '61.135.169.121'
# 可以切换的wifi
wifiList = ['Tenda_D05B41', 'Tenda_D05B40', 'Tenda_D05B42']


# 获取当前时间
def get_time():
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())


# 获取当前wifi
def get_current_wifi():
    cmd = 'netsh wlan show interfaces'
    p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    ret = p.stdout.read()
    index = ret.decode(encoding='unicode_escape').find("SSID")
    if index > 0:
        return ret[index:].decode(encoding='unicode_escape').split(':')[1].split('\r\n')[0].strip()
    else:
        return None


# 测试能否ping通
def check_ping(ip, count=1, timeout=500):
    cmd = 'ping -n %d -w %d %s > NUL' % (count, timeout, ip)
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'


# 自动切换wifi
def auto_switch_wifi(wifiList):
    wifi = random.choice(wifiList)
    cmd = 'netsh wlan connect name={}'.format(wifi)
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'


def main():
    while True:
        current_wifi = get_current_wifi()
        print("当前的wifi为：", current_wifi)
        t = time.time()
        if check_ping(ipTest, 2) != 'ok':
            print(get_time(), " - 联网失败，正在切换wifi: ", current_wifi)
            if auto_switch_wifi(wifiList) == 'ok':
                print("切换成功")
                print("-" * 40)
            else:
                continue
            time.sleep(10)
        else:
            print(get_time(), " - 可以成功联网")
            print('-' * 40)
            time.sleep(10)
            # os.system('cls')


if __name__ == "__main__":
    main()
