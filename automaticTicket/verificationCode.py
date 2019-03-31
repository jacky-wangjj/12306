#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------
# Author:   wangjj17
# Name:     verificationCode
# Date:     2019/3/31
# -------------------------
import base64
import random
import time

import requests

session = requests.Session()
headers = {
        'Host': 'kyfw.12306.cn',
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

def get_code():
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'
    random_data = random.random()
    params = {
        'login_site': 'E',
        'module': 'login',
        'rand': 'sjrand',
        '_': random_data,
    }
    response = session.get(url, params=params, headers=headers)
    data = response.json()
    image = data['image']
    image = base64.b64decode(image)
    with open(r'code.png','wb') as f:
        f.write(image)
    print("成功下载验证码到本地")

if __name__ == "__main__":
    get_code()