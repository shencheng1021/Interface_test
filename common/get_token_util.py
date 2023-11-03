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

    def get_access_token(self,key,username):
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
        YamlUtil().write_yaml({'access_token_'+key: result['access_token']})

    def get_token(self,key,username):
        GetToken().get_access_token(key,username)
        url='http://172.24.100.75:10006/expose/website/newLoginByCenter'
        method='get'
        accessToken=YamlUtil().read_yaml('access_token_'+key)
        data={
            'Accept': 'application/json, text/plain, */*',
            'accessToken' : accessToken
        }
        rep=RequestsUtil().send_request(method=method,url=url,params=data)
        result = json.loads(rep)
        GmSsl().set_token(key,result['data'])


if __name__ == '__main__':
    GetToken().get_token('tt','17754124411')
