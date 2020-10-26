"""
Windows自动切换WiFi v0.2.1

- 日志优化
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
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 获取当前日期
def get_day():
    return datetime.datetime.now().strftime('%Y.%m.%d')


# 日志收集
def log(msg, is_output):
    log_str = get_time() + ' - ' + msg
    # 打开文件 如果文件不存在则创建 将光标放在文件末尾
    log_file = open("./log/log-" + get_day(), mode='a', encoding='utf8')
    log_file.write(log_str + "\n")  # 写入一行数据
    log_file.close()  # 关闭文件
    if is_output == 'true':  # 是否打印到控制台
        print(log_str)


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
    log("执行命令: " + cmd, 'false')
    res = os.system(cmd)
    if res == 0:
        log("可以正常联网, 当前wifi为: " + str(get_current_wifi()), "false")
    return 'ok' if res == 0 else 'failed'


# 切换wifi
def auto_switch_wifi(wifi):
    # wifi = random.choice(wifi_list)  # 从wifi列表中随机选择一个wifi
    cmd = 'netsh wlan connect name={}'.format(wifi)
    log("执行命令: " + cmd, 'true')
    # log("执行: " + "\033[31m" + cmd + "\033[0m")
    res = os.system(cmd)
    if check_ping(random.choice(BaiduIP), 2) != 'ok':
        # time.sleep(0.5)
        log("可以正常联网, 当前wifi为: " + str(get_current_wifi()), 'false')
        print('-' * 70)
    return 'ok' if res == 0 else 'failed'


def main():
    log("程序开始, 当前wifi为: " + str(get_current_wifi()), "true")
    while True:
        if check_ping(random.choice(BaiduIP), 2) != 'ok':  # 测试能否ping通
            wifi = random.choice(wifiList)  # 从wifi列表中随机选择一个wifi
            log("联网失败, 正在切换wifi: " + wifi, 'true')
            if auto_switch_wifi(wifi) != 'ok':
                continue
        time.sleep(10)  # 休眠10秒


def test():
    check_ping(random.choice(BaiduIP), 2)


if __name__ == "__main__":
    main()
