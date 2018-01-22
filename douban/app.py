# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import json


def run():
    # 先进入登录页面
    url = "https://accounts.douban.com/login"
    username = "18650078754"
    password = "zhu5530"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rep = requests.get(soup.find(id="captcha_image").get("src"))
    with open("codeImg/code.png","wb") as f:
        f.write(rep.content)
    captcha_id = soup.find("input",attrs={"name":"captcha-id"})
    print(captcha_id)

if __name__ == "__main__":
    run()
