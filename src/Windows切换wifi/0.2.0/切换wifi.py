"""
Windows自动切换WiFi v0.1.2
    原始代码来自于: https://blog.csdn.net/qq_34377830/article/details/82497457
重构ing...
时间精确到毫秒
"""
import datetime
import os
import subprocess
import random
import time

# 百度ip
BaiduIP = ['61.135.169.121', '182.61.200.7']

# 可以切换的wifi列表
wifiList = ['Tenda_D05B40', 'Tenda_D05B41', 'Tenda_D05B42']


# 获取当前时间
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]


# 控制台日志
def log(msg):
    print(get_time(), ' - ', msg)


# 获取当前wifi
def get_current_wifi():
    cmd = 'netsh wlan show interfaces'
    # subprocess.Popen() 可以将cmd命令的执行结果返回出来
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    ret = p.stdout.read()
    index = ret.decode(encoding='unicode_escape').find("SSID")
    if index > 0:  # 获取到 SSID , 将SSID的值剪切出来
        return ret[index:].decode(encoding='unicode_escape').split(':')[1].split('\r\n')[0].strip()
    else:
        return None


# 测试能否ping通
def check_ping(ip, count=1, timeout=500):
    cmd = 'ping -n %d -w %d %s > NUL' % (count, timeout, ip)
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'


# 切换wifi
def auto_switch_wifi(wifi):
    # wifi = random.choice(wifi_list)  # 从wifi列表中随机选择一个wifi
    cmd = 'netsh wlan connect name={}'.format(wifi)
    res = os.system(cmd)
    if res == 0:
        print("切换成功")
    return 'ok' if res == 0 else 'failed'


def main():
    while True:
        print("当前的wifi为：", get_current_wifi())  # 获取当前连接wifi
        random.choice(BaiduIP)
        if check_ping(BaiduIP, 2) == 'ok':  # ping百度ip能否ping通
            wifi = random.choice(wifiList)  # 从wifi列表中随机选择一个wifi
            log("联网失败, 正在切换wifi: " + wifi)
            if auto_switch_wifi(wifi) != 'ok':
                continue
        else:
            log("可以成功联网")
        print('-' * 60)
        time.sleep(10)


if __name__ == "__main__":
    main()
