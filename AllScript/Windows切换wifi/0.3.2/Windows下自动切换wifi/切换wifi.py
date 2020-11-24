"""
Windows自动切换WiFi v0.2.1
    此脚本仅适用于Windows环境下

- 日志优化
"""
import datetime
import os
import subprocess
import random
import time

import sys

sys.path.append(r"/AllScript\Windows切换wifi\0.3.2\Windows下自动切换wifi")

# 可以切换的wifi列表
wifiList = [
    'Tenda_D05B40',
    'Tenda_D05B41',
    'Tenda_D05B42'
]

# 当前连接的wifi
current_wifi = ""


# 获取当前时间
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 获取当前日期 用于生成日志文件名称
def get_day():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def write_log_file(msg):
    log_str = get_time() + ' - ' + msg
    # 打开文件 如果文件不存在则创建 将光标放在文件末尾
    log_file = open("./log/" + get_day() + ".log", mode='a', encoding='utf8')
    log_file.write(log_str + "\n")  # 写入一行数据
    log_file.close()  # 关闭文件
    return log_str  # 返回写入文件的字符串


# 日志收集
def log(msg, is_output):
    if is_output:  # 是否打印到控制台
        print(write_log_file(msg))
    else:
        write_log_file(msg)


def exec_cmd(cmd):
    # subprocess.Popen() 可以将cmd命令的执行结果返回出来
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    result = p.stdout.read().decode(encoding='gbk')
    return result


# 获取当前wifi
def get_current_wifi():
    cmd = 'netsh wlan show interfaces'
    log("执行命令: " + cmd, False)
    result = exec_cmd(cmd)
    index = result.find("SSID")
    if index > 0:  # 获取到 SSID , 将SSID的值剪切出来
        current_wifi = result[index:].split(':')[1].split('\r\n')[0].strip()
        return current_wifi
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
    if check_ping("baidu.com", 2) != 'ok':
        log("可以正常联网, 当前wifi为: " + str(get_current_wifi()), 'false')
        print('-' * 70)
    return 'ok' if res == 0 else 'failed'


def main():
    log("程序开始, 当前wifi为: " + str(get_current_wifi()), "true")
    while True:
        if check_ping("baidu.com", 2) != 'ok':  # 测试能否ping通
            wifi = random.choice(wifiList)  # 从wifi列表中随机选择一个wifi
            log("联网失败, 正在切换wifi: " + wifi, 'true')
            if auto_switch_wifi(wifi) != 'ok':
                continue
        time.sleep(10)  # 休眠10秒


def test():
    file_list = [
        "D:/Test/test1.txt",
        "D:/Test/test2.txt",
        "D:/Test/test3.txt",
        "D:/Test/test4.txt",
        "D:/Test/test5.txt",
        "D:/Test/test6.txt",
        "D:/Test/test7.txt",
    ]


if __name__ == "__main__":
        main()
