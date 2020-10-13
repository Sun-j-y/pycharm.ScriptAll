"""
校园网自动登录 v0.0.1
    原始代码来自于 https://sunlanchang.github.io/2017/10/31/%E6%A0%A1%E5%9B%AD%E7%BD%91%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95%E8%84%9A%E6%9C%AC/
校园网登陆网址
    http://172.168.254.6/a70.htm?wlanuserip=172.19.219.87&wlanacname=&wlanacip=172.168.254.100&mac=000000000000

"""
import os

import requests

RequestURL = 'http://172.168.254.6:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.168.254.6&iTermType=1&wlanuserip=172.19.219.87&wlanacip=172.168.254.100&mac=000000000000&ip=172.19.65.99&enAdvert=0&loginMethod=1'
RequestMethod = 'POST'

RequestHeader = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application',
    'Cookie': 'program=aygxy; vlan=0; PHPSESSID=4kmcof308gdhd272bbn5ja20t6; md5_login=18031210211%7C888888; ip=172.19.65.99; is_login=1; areaID=wlanuserip%3D172.19.219.87',
    'DNT': '1',
    'Host': '172.168.254.6:801',
    'Origin': 'http://172.168.254.6',
    'Referer': 'http://172.168.254.6/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
BaiduIP = '182.61.200.7'
EduIP = '172.168.254.6'

url = 'http://210.31.32.126/cgi-bin/do_login'


# 登录 浏览器头信息用来伪装浏览器
def login():
    postdata = {'username': '你的校园网账号',
                'password': '{TEXT}你的密码',
                'drop': '0',
                'type': '1',
                'n': '100'}
    headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Length': '65',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'PHPSESSID=a70fr8pfvhhtt329qvb21p7ka6',
               'Host': '210.31.32.126',
               'Origin': 'http://210.31.32.126',
               'Referer': 'http://210.31.32.126/',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    requests.post(url, data=postdata)


# 查看连接的是否是校园网
def is_connect_edu():
    status_code = requests.get(url).status_code
    if status_code == 200:
        return True
    else:
        return False


# 是否连上网
def is_connect_web():
    r = requests.get("http://www.baidu.com").text
    print(type(r))
    if r.find('210.31.32.126') != -1:
        return False
    else:
        return True


def check_ping(ip, count=1, timeout=500):
    cmd = 'ping -n %d -w %d %s > NUL' % (count, timeout, ip)
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'


# 直到校园网连接上为止
# while True:
#     if is_connect_edu():  # 是否连接上校园网
#         if not is_connect_web():  # 是否连接上外网
#             login()
#             if requests.get('http://www.baidu.com').status_code == 200:
#                 print('Already connected Internet')
#             else:
#                 print('Not connected Internet')
#         break

print(check_ping(BaiduIP))
print(check_ping(EduIP))

if check_ping(EduIP) == 'ok':  # 能ping通校园网
    if check_ping(BaiduIP) == 'failed':  # ping不通百度 登陆校园网
        login()
        if check_ping(BaiduIP) == 'ok':
            print("已连上网络")
