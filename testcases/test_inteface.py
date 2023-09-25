# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 接口测试自动化测试脚本
@time: 2023/9/25 14:25
"""

import requests


class TestInterface:

    access_token="",
    cookies="",
    session=requests.session()


    def test_login(self):
        url='http://172.24.100.107:14000/auth/oauth/token?grant_type=mobile&source=PORTAL_CONFIG'
        data={
            'mobile':'SMSCUST%4017754754412',
            'code':'230516'
        }
        headers={
            "enterCode":"TLSK",
            "Accept":"application/json, text/plain, */*",
            "Authorization":"Basic dG9uZ0xpYW46dG9uZ0xpYW4=",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"172.24.100.107:14000",
            "Origin":"http://172.24.100.107:14000"

        }

        rep=requests.request('post',url=url,data=data,headers=headers)
        TestInterface.access_token=rep.json()['access_token']
        TestInterface.cookies = rep.cookies
        print(TestInterface.cookies.values())


    def test_newLoginByCenter(self):
        url="http://172.24.100.75:10006/expose/website/newLoginByCenter"
        data={
            "Accept":"application/json, text/plain, */*",
            "accessToken":TestInterface.access_token
        }
        rep=requests.request("get",url=url,params=data)
        print(rep.json())
        TestInterface.cookies = rep.cookies
        print(TestInterface.cookies.values())



    def test_get_traders(self):
        url="http://172.24.100.75:10006/expose/website/traders"
        headers={
            "Host":"172.24.100.75:10006",
            "Cookie":TestInterface.cookies
        }
        print(TestInterface.cookies)
        rep=requests.request("get",url=url,headers=headers,cookies=TestInterface.cookies)
        print(rep.status_code)
        print(rep.json())

