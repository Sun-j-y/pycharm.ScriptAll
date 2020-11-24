#!/usr/bin/python3
# -*- coding: utf-8 -*-
import base64
import requests

# 此处根据自己校园网Form Data中发送的数据进行更改
action = 'login'
username = '用户名'
password = '密码'
ac_id = '1'
user_ip = '127.131.1.1'

# 登录地址
post_addr = "http://172.168.254.6/"
# 构造头部信息 注意Cookie可能十分重要，而且Cookie会有过期时间（我们学校过期时间是1个月），过期之后，可能需要复制新的Cookie替换。
post_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'http://wlrz.fudan.edu.cn',
    'Referer': 'http://wlrz.fudan.edu.cn/srun_portal_pc.php?ac_id=1&&phone=1',
    'Content-Length': '112',
    'Cookie': 'login=YUtl4F5w2GWDfWUA8O**********0MDW7tX1eoOzS00eusx19E0245ORqeeZHVwBzEd1DGI%253D',
    'Host': 'wlrz.fudan.edu.cn',
    'Connection': 'keep-alive',
}

post_data = {
    'action': action,
    'username': username,
    'password': password,
    'ac_id': ac_id,
    'user_ip': user_ip
}

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

# 发送post请求登录网页
z = requests.post(post_addr, data=post_data, headers=request_headers)
# s = z.text.encode('utf8')
# print(s)
print("login success!")
input("任意键继续...")
