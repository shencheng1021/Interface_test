# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 接口测试自动化测试脚本
@time: 2023/9/25 14:25
"""

import requests

from common.config import ConfigParser
from common.gmssl_util import GmSsl


class TestInterface:

    access_token="",
    session=requests.session()


    def test_login(self):
        url='http://172.24.100.107:14000/auth/oauth/token?grant_type=mobile&source=PORTAL_CONFIG'
        data={
            'mobile':'SMSCUST%4017754754412',
            'code':'230516'
        }
        headers={
            "enterCode":"TLSK",
            "Authorization":"Basic dG9uZ0xpYW46dG9uZ0xpYW4=",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"172.24.100.107:14000",
        }

        rep=requests.request('post',url=url,data=data,headers=headers)
        TestInterface.access_token=rep.json()['access_token']



    def test_newLoginByCenter(self):
        url="http://172.24.100.75:10006/expose/website/newLoginByCenter"
        data={
            "Accept":"application/json, text/plain, */*",
            "accessToken":TestInterface.access_token
        }
        rep=requests.request("get",url=url,params=data)
        GmSsl().get_token(rep.json()['data'])


    def test_get_traders(self):
        url="http://172.24.100.75:10006/expose/website/traders"
        headers={
            "Host":"172.24.100.75:10006",
            "Cookie": "Token="+ConfigParser().cget('interfacetoken','token','interface_config')
        }
        rep=requests.request("get",url=url,headers=headers)
        print(rep.status_code)
        print(rep.json())


    def test_getmenus(self):
        url="http://172.24.100.75:10006/expose/website/getMenus"
        headers={
            "Host": "172.24.100.75:10006",
            "Cookie": "Token=" + ConfigParser().cget('interfacetoken', 'token', 'interface_config'),
            "Token": ConfigParser().cget('interfacetoken','token','interface_config')
        }
        rep=requests.request("get",url=url,headers=headers)
        print(rep.json())


if __name__ == '__main__':
    TestInterface()