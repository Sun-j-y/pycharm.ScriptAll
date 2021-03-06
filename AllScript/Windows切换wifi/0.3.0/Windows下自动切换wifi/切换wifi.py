"""
Windows自动切换WiFi v0.2.1

- 日志系统更新 控制台只打印错误信息,全部日志信息存入log文件夹下
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


# 控制台日志
def log(msg, isError):
    log_str = get_time() + ' - ' + msg
    log_file = open("./log/log-" + get_day(), mode='a', encoding='utf8')
    log_file.write(log_str + "\n")
    log_file.close()
    if isError == 'true':
        print(log_str)

    # print("\033[32m" + get_time() + "\033[0m", ' - ', msg)


# log()重载 打印特定颜色的日志
# def log(msg, color):
#     if color == 'RED':
#         print("", msg)


# 获取当前时间
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_day():
    return datetime.datetime.now().strftime('%Y.%m.%d')


# def get_time(format):
#     return datetime.datetime.now().strftime(format)[:-3]


# 获取当前wifi
def get_current_wifi():
    cmd = 'netsh wlan show interfaces'
    # log("执行: " + "\033[31m" + cmd + "\033[0m")
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
    # log("执行: " + "\033[31m" + cmd + "\033[0m")
    log("执行: " + cmd, 'false')
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'


# 切换wifi
def auto_switch_wifi(wifi):
    # wifi = random.choice(wifi_list)  # 从wifi列表中随机选择一个wifi
    cmd = 'netsh wlan connect name={}'.format(wifi)
    log("执行: " + cmd, 'true')
    # log("执行: " + "\033[31m" + cmd + "\033[0m")
    res = os.system(cmd)
    if check_ping(random.choice(BaiduIP), 2) != 'ok':
        log("可以正常联网", 'false')
        print('-' * 70)
    return 'ok' if res == 0 else 'failed'


def main():
    log("程序开始", "true")
    while True:
        if check_ping(random.choice(BaiduIP), 2) != 'ok':  # 测试能否ping通
            wifi = random.choice(wifiList)  # 从wifi列表中随机选择一个wifi
            log("联网失败, 正在切换wifi: " + wifi, 'true')
            if auto_switch_wifi(wifi) != 'ok':
                continue
        time.sleep(10)
        # # 不能: 切换wifi
        # # 能: 继续下次循环


if __name__ == "__main__":
    main()
