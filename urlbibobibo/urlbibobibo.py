import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and len(response.content)>0:
            print(f"{url} 有效")
        else:
            print(f"{url} 无效。 状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"{url} 无效. 报错: {e}")

with open("url.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    check_website(url.strip())