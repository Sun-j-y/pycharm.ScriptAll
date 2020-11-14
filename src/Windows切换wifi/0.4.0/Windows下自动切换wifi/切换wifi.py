"""
Windows自动切换WiFi v0.4.0
    此脚本仅适用于Windows环境下 python
    可连接wifi列表应为已保存并且再当前位置可连接得到的wifi的SSID

- 日志简化 去除大量无用日志
"""
import datetime
import os
import subprocess
import random
import time

# 可以切换的wifi列表
_wifi_list = [
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


# 日志收集
def log(msg, is_output=True):
    # # 拼接打印信息
    log_str = get_time() + ' - ' + msg
    # # 打开文件 如果文件不存在则创建 将光标放在文件末尾
    log_file = open("./log/" + get_day() + ".log", mode='a', encoding='utf8')
    log_file.write(log_str + "\n")  # 写入一行数据
    log_file.close()  # 关闭文件

    if is_output:  # 打印到控制台
        print(log_str)


def exec_cmd(cmd, is_result=True):
    if is_result:
        result = os.system(cmd)
    else:
        # subprocess.Popen() 可以将cmd命令的执行结果返回出来
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        result = p.stdout.read().decode(encoding='gbk')
    return result


# 获取当前wifi
def get_current_wifi():
    result = exec_cmd('netsh wlan show interfaces', False)
    index = result.find("SSID")
    if index > 0:  # 获取到 SSID , 将SSID的值剪切出来
        current_wifi = result[index:].split(':')[1].split('\r\n')[0].strip()
        return current_wifi
    else:
        return None


# 测试能否ping通指定ip
def check_ping(ip, count=1, timeout=500):
    res = os.system('ping -n %d -w %d %s > NUL' % (count, timeout, ip))
    if res == 0:
        log("可以正常联网, 当前wifi为: " + str(get_current_wifi()), False)
    return 'ok' if res == 0 else 'failed'


# 切换wifi
def auto_switch_wifi(wifi):
    # wifi = random.choice(wifi_list)  # 从wifi列表中随机选择一个wifi
    res = os.system('netsh wlan connect name={}'.format(wifi))
    if check_ping("baidu.com", 2) != 'ok':
        log("切换成功", False)
        print('-' * 70)
    return 'ok' if res == 0 else 'failed'


def main():
    log("------------------脚本开始执行------------------")
    log("当前wifi: " + str(get_current_wifi()) + ", 正在检测...")
    while True:
        if check_ping("baidu.com", 2) != 'ok':  # 不能够ping通
            wifi = random.choice(_wifi_list)  # 从wifi列表中随机选择一个wifi
            log("联网失败, 正在切换wifi: " + wifi)
            if auto_switch_wifi(wifi) != 'ok':
                continue
        time.sleep(9)  # 休眠 参数单位为秒


def test():
    print(exec_cmd("netsh wlan connect name=Tenda_D05B40"))


if __name__ == "__main__":
    main()
