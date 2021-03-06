import time

import requests

RequestURL = 'http://172.168.254.6:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.168.254.6&iTermType=1&wlanuserip=172.19.219.87&wlanacip=172.168.254.100&mac=000000000000&ip=172.19.65.99&enAdvert=0&loginMethod=1'
# 此处根据自己校园网Form Data中发送的数据进行更改
action = 'login'
username = '用户名'
password = '密码'
ac_id = '1'
user_ip = '127.131.1.1'
post_data = {
    'DDDDD': '%2C0%2C18031210211%40yidong',
    'upass': '888888',
    'R1': '0',
    'R2': '0',
    'R6': '0',
    'para': '00',
    '0MKKey': '123456',

}
#      "DDDDD=%2C0%2C学号%40运营商&upass=密码&R1=0&R2=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login="
data = "DDDDD=%2C0%2C18031210211%40yidong&upass=888888&R1=0&R2=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login="
#      http://172.168.254.6:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.168.254.6&iTermType=1&wlanuserip=${本地ip}&wlanacip=172.168.254.100&mac=000000000000&ip=${本地ip}&enAdvert=0&loginMethod=1
url = "http://172.168.254.6:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.168.254.6&iTermType=2&wlanuserip=172.19.192.251&wlanacip=172.168.254.100&mac=000000000000&ip=172.19.192.251&enAdvert=0&loginMethod=1"
request_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '160',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'program=aygxy; vlan=0; PHPSESSID=4kmcof308gdhd272bbn5ja20t6; md5_login=18031210211%7C888888; ip=172.19.192.251; areaID=wlanuserip%3D172.19.219.87; is_login=1',
    'DNT': '1',
    'Host': '172.168.254.6:801',
    'Origin': 'http://172.168.254.6',
    'Referer': 'http://172.168.254.6/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
form_data = {

    'DDDDD': ',0,18031210211@yidong',
    'upass': '888888',
    'R1': '0',
    'R2': '0',
    'R6': '0',
    'para': '00',
    '0MKKey': '123456',
    'buttonClicked': '',
    'redirect_url': '',
    'err_flag': '',
    'username': '',
    'password': '',
    'user': '',
    'cmd': '',
    'Login': '',
}
BaiduIP = '182.61.200.7'
EduIP = '172.168.254.6'

url = 'http://172.168.254.6/'


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

print("ping Baidu - " + check_ping(BaiduIP))
print("ping edu - " + check_ping(EduIP))

if check_ping(EduIP) == 'ok':  # 能ping通校园网
    while True:
        print("login...")
        if check_ping(BaiduIP) == 'failed':  # ping不通百度 登陆校园网
            requests.post(url, data=data)
            time.sleep(1)  # 休眠
        if check_ping(BaiduIP) == 'ok':
            print("已连上网络")
            break
        time.sleep(1)  # 休眠
else:
    print("未连接校园网...")
