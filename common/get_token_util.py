# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 获取接口中鉴权的token公共方法
@time: 2022/4/13 9:34
"""
import json

from common.gmssl_util import GmSsl
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil


class GetToken:

    def get_access_token(self,username):
        url='http://172.24.100.107:14000/auth/oauth/token?grant_type=mobile&source=PORTAL_CONFIG'
        method= 'post'
        headers={
            'enterCode': 'TLSK',
            'Authorization' : 'Basic dG9uZ0xpYW46dG9uZ0xpYW4=',
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Host' : '172.24.100.107:14000'
        }
        data={
            'mobile': 'SMSCUST%40' + username,
            'code': '230516'
        }
        rep=RequestsUtil().send_request(method=method,url=url,headers=headers,data=data)
        result = json.loads(rep)
        YamlUtil().write_yaml({'access_token': result['access_token']})

    def get_token(self,username):
        YamlUtil().clear_yaml()
        GetToken().get_access_token(username)
        url='http://172.24.100.75:10006/expose/website/newLoginByCenter'
        method='get'
        accessToken=YamlUtil().read_yaml('access_token')
        data={
            'Accept': 'application/json, text/plain, */*',
            'accessToken' : accessToken
        }
        rep=RequestsUtil().send_request(method=method,url=url,params=data)
        result = json.loads(rep)
        GmSsl().set_token(result['data'])


if __name__ == '__main__':
    GetToken().get_token('17754124411')
