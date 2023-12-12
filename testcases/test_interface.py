# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 接口测试自动化测试脚本
@time: 2023/9/25 14:25
"""
import json
import logging
import pytest
from common.assert_util import AssertUtil
from common.logger_util import Logger
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil
import allure

from common.get_token_util import GetToken

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)



@allure.feature("砼联数科官网接口测试")
class TestInterface:

    # @allure.title("获取access_token")
    # @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_access_token.yml'))
    # def test_get_access_token(self,caseinfo):
    #
    #     url=caseinfo['requests']['url']
    #     data=caseinfo['requests']['data']
    #     headers=caseinfo['requests']['headers']
    #     method=caseinfo['requests']['method']
    #     log.logger.info("请求头：%s" % headers)
    #     log.logger.info("请求数据：%s" % data)
    #     result=RequestsUtil().send_request(method,url,data=data,headers = headers)
    #     result=json.loads(result)
    #     YamlUtil().write_yaml({'access_token':result['access_token']})
    #     AssertUtil().assertIn('access_token',result)
    #     AssertUtil().assertEqual('TLSK',result['loginEnterCode'])
    #     #assert 'access_token' in result
    #     # assert 'token_type' in result
    #     # assert 'expires_in' in result
    #     # assert 'scope' in result
    #     # assert result['loginEnterCode'] == 'TLSK'
    #     # assert 'license' in result
    #
    # @allure.title("登录接口，获取接口返回的token")
    # @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_token.yml'))
    # def test_get_token(self,caseinfo):
    #     url=caseinfo['requests']['url']
    #     caseinfo['requests']['data']['accessToken'] = YamlUtil().read_yaml('access_token')
    #     data=caseinfo['requests']['data']
    #     method = caseinfo['requests']['method']
    #     log.logger.info("请求数据：%s" % data)
    #     result = RequestsUtil().send_request(method,url,params=data)
    #     result=json.loads(result)
    #     GmSsl().set_token(result['data'])
    #     AssertUtil().assertEqual('登录成功',result['msg'])
        #assert '登录成功' == result['msg']
    @allure.title("登录接口，获取接口返回的token")
    def test_get_token(self):
        GetToken().get_token('user','17754754412')

    @allure.title("查询账户关联的企业列表")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_traders.yml'))
    def test_get_traders(self,caseinfo):
        url = caseinfo['requests']['url']
        caseinfo['requests']['headers']['Cookie'] = "Token="+YamlUtil().read_yaml('token_user')
        headers = caseinfo['requests']['headers']
        method = caseinfo['requests']['method']
        log.logger.info("请求头：%s" % headers)
        rep = RequestsUtil().send_request(method,url,headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual('TN2023030800027204', result['data'][0]['traderNo'])
        #assert 'TN2023030800027204' == result['data'][0]['traderNo']

    @allure.title("查询当前账户商户中心菜单权限")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_menus.yml'))
    def test_get_menus(self,caseinfo):
        url=caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token=YamlUtil().read_yaml('token_user')
        caseinfo['requests']['headers']['Cookie'] = "Token=" + token
        caseinfo['requests']['headers']['Token'] = token
        headers=caseinfo['requests']['headers']
        log.logger.info("请求头：%s" % headers)
        rep=RequestsUtil().send_request(method,url,headers=headers)
        result=json.loads(rep)
        AssertUtil().assertEqual("操作成功",result['msg'])
        #assert '操作成功' == result['msg']

if __name__ == '__main__':
    pytest.main()