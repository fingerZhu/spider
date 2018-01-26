# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import json
import pytesseract
from PIL import Image
from PIL import ImageFilter
import os
from PIL import ImageEnhance


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

def test():
    R,G,B = 0,1,2
    infile = "codeImg/code.png"
    f,ext = os.path.splitext(infile)
    img = Image.open(infile).point(lambda x:0 if x<143 else 255,"1")
    img.show()





if __name__ == "__main__":
    test()
