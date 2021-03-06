# coding: utf-8
from urllib import request, parse
from configparser import ConfigParser


# 从配置文件读取账号密码
cf = ConfigParser()
cf.read('config.ini')
username = cf.get('account', 'username')
password = cf.get('account', 'password')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
}


def logout():
    url = 'http://ipgw.neu.edu.cn/include/auth_action.php'

    params = {
        'action': 'logout',
        'username': username,
        'password': password,
        'ajax': '1',
    }

    data = parse.urlencode(params).encode(encoding='utf-8')
    req = request.Request(url=url, data=data, headers=headers, method='POST')
    res = request.urlopen(req, timeout=15)
    if res.getcode() != 200:
        print('操作失败')
    else:
        print('操作成功')


if __name__ == "__main__":
    logout()
