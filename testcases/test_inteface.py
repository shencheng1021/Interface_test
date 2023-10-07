# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 接口测试自动化测试脚本
@time: 2023/9/25 14:25
"""
import json

import requests
import pytest
from common.config import ConfigParser
from common.gmssl_util import GmSsl
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil


class TestInterface:

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('get_access_token.yml'))
    def test_get_access_token(self,caseinfo):

        url=caseinfo['requests']['url']
        data=caseinfo['requests']['data']
        headers=caseinfo['requests']['headers']
        method=caseinfo['requests']['method']
        result=RequestsUtil().send_request(method,url,data=data,headers = headers)
        result=json.loads(result)
        YamlUtil().write_yaml({'access_token':result['access_token']})
        assert 'access_token' in result
        assert 'token_type' in result
        assert 'expires_in' in result
        assert 'scope' in result
        assert result['loginEnterCode'] == 'TLSK'
        assert 'license' in result



    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('get_token.yml'))
    def test_get_token(self,caseinfo):
        url=caseinfo['requests']['url']
        caseinfo['requests']['data']['accessToken'] = YamlUtil().read_yaml('access_token')
        data=caseinfo['requests']['data']
        method = caseinfo['requests']['method']
        result = RequestsUtil().send_request(method,url,params=data)
        result=json.loads(result)
        GmSsl().set_token(result['data'])
        assert '登录成功' == result['msg']


    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('get_traders.yml'))
    def test_get_traders(self,caseinfo):
        url = caseinfo['requests']['url']
        caseinfo['requests']['headers']['Cookie'] = "Token="+YamlUtil().read_yaml('token')
        headers = caseinfo['requests']['headers']
        method = caseinfo['requests']['method']
        result = RequestsUtil().send_request(method,url,headers=headers)
        result=json.loads(result)
        assert 'TN2023030800027204' == result['data'][0]['traderNo']

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('get_menus.yml'))
    def test_get_menus(self,caseinfo):
        url=caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        caseinfo['requests']['headers']['Cookie'] = "Token=" + YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Token'] = YamlUtil().read_yaml('token')
        headers=caseinfo['requests']['headers']
        result=RequestsUtil().send_request(method,url,headers=headers)
        result=json.loads(result)
        assert '操作成功' == result['msg']

if __name__ == '__main__':
    pytest.main()