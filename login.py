#!/bin/python3
# coding: utf-8

"""
测试
"""

__author__ = "bovenson"
__email__ = "szhkai@qq.com"
__date__ = "2018-04-24 14:55"

from urllib import request, parse
from configparser import ConfigParser


# 从配置文件读取账号密码
cf = ConfigParser()
cf.read('config.ini')
username = cf.get('account', 'username')
password = cf.get('account', 'password')

headers_pc = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    # 'Host': 'ipgw.neu.edu.cn',
    # 'Origin': 'https://ipgw.neu.edu.cn',
    # 'Referer': 'https://ipgw.neu.edu.cn/srun_portal_pc.php?url=&ac_id=1',
}

headers_phone = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3 ',
}

url = 'http://ipgw.neu.edu.cn'
url_pc = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1'
url_phone = 'http://ipgw.neu.edu.cn/srun_portal_phone.php?ac_id=1'

login_params = {
    'action': 'login',
    'ac_id': 1,
    'user_ip': '',
    'nas_ip': '',
    'user_mac': '',
    'url': '',
    'username': username,
    'password': password,
    'save_me': 0,
}


def is_login(html_content):
    if '用户不存在' in html_content:
        return '用户不存在'
    elif '密码错误' in html_content:
        return '密码错误'
    elif '已经在线了' in html_content:
        return '已经在线了'
    elif '网络已连接' in html_content or ('注销' in html_content and '登录' not in html_content):
        return '网络已连接'
    return '*' * 100 + '\n\n' + html_content + '\n\n' + '*' * 100 + '\n'


def login(phone=False):
    data = parse.urlencode(login_params).encode(encoding='utf-8')
    if phone:
        req = request.Request(url=url_phone, data=data, headers=headers_phone, method='POST')
    else:
        req = request.Request(url=url_pc, data=data, headers=headers_pc, method='POST')
    res = request.urlopen(req, timeout=15)
    msg = is_login(res.read().decode('utf-8'))
    if res.getcode() == 200:
        print(msg)
    else:
        print('请求错误: ', res.getcode())


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] in ['mobile', 'phone', 'android', 'ios']:
        login(True)
    else:
        login()
