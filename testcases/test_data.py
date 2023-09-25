# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time

import requests


def test111():
    response = requests.get('http://172.24.100.75:10006/#/login')
    cookie = response.cookies.get_dict()
    print(cookie)
