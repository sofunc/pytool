import requests
from bs4 import BeautifulSoup
import os
import sys

url = sys.argv[1]  # 获取命令行参数
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

image_urls = soup.find_all("img")

os.mkdir("images")

for image in image_urls:
    src = image["src"]
    image_response = requests.get(src)
    image_name = src.split("/")[-1]
    f = open("images/"+image_name, "wb")
    f.write(image_response.content)
    f.close()