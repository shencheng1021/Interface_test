# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 保理E产品接口测试
@time: 2023/10/27 16:30
"""
import json
import time

import allure
import pytest

from common.assert_util import AssertUtil
from common.gmssl_util import GmSsl
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil
from common.get_token_util import GetToken


class TestBle:

    def test_get_token(self):
        GetToken().get_token('13475475547')

    @allure.title('查看数据授权协议接口')
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('ble_showAgreement.yml'))
    def test_showAgreement(self,caseinfo):
        url=caseinfo['requests']['url']
        method=caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers=caseinfo['requests']['headers']
        data=caseinfo['requests']['data']
        rep=RequestsUtil().send_request(method,url,params=data,headers=headers)
        result=json.loads(rep)
        AssertUtil().assertEqual('不需要展示',result['msg'])

    @allure.title('同意数据授权协议接口')
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('ble_agreeAgreement.yml'))
    def test_agreeAgreement(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, params=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual('操作成功', result['msg'])

    @allure.title('查看该用户是否为核心企业')
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('ble_identity_check.yml'))
    def test_identity_check_fkdl(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        rep = RequestsUtil().send_request(method, url, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual('查询完成,已完成准入', result['msg'])

    @allure.title('查看该核心企业密钥信息完善接口')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_applycheck.yml'))
    def test_applyCheck(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = GmSsl().gmssh_encrypt(caseinfo['requests']['data'])
        rep = RequestsUtil().send_request(method, url, json=data,headers=headers)
        result=GmSsl().gmssh_decode(rep)
        AssertUtil().assertEqual(caseinfo['assert'], result['canAccess'])

    @allure.title('查看该核心企业供应商列表查询接口')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_suplist.yml'))
    def test_supplier_list(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, params=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual(40, result['data']['total'])

    @allure.title('按照名称模糊查询供应商接口')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_ListTraderOfFinance.yml'))
    def test_listTraderOfFinance(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data=GmSsl().gmssh_encrypt(caseinfo['requests']['data'])
        rep = RequestsUtil().send_request(method, url, json=data, headers=headers)
        result=GmSsl().gmssh_decode(rep)
        AssertUtil().assertEqual(4,result['list']['total'])

    @allure.title('在供应商列表中新增供应商接口')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_addSupplier.yml'))
    def test_add_supplier(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, json=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual(caseinfo['assert'],result['msg'])

    @allure.title('在供应商列表中删除供应商接口')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_delSupplier.yml'))
    def test_del_supplier(self, caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, params=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual(caseinfo['assert'], result['msg'])

    @allure.title('新增融信签发')
    @pytest.mark.usefixtures('oa_information_initialization')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_addissued.yml'))
    def test_add_issued(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, json=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual(caseinfo['assert'], result['msg'])

    @allure.title('查询融信签发列表')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_signedList.yml'))
    def test_signedList(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, params=data, headers=headers)
        result = json.loads(rep)
        YamlUtil().write_yaml({'creditNo' : result['data']['list'][0]['serialNo']})
        AssertUtil().assertEqual(caseinfo['assert'], result['msg'])

    @allure.title('查询关联融信的OA审核信息')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_oaList.yml'))
    def test_oaList(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        caseinfo['requests']['data']['creditNo']=YamlUtil().read_yaml('creditNo')
        data=caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, params=data, headers=headers)
        result = json.loads(rep)
        YamlUtil().write_yaml({'oaid': [result['data'][0]['id']]})
        AssertUtil().assertEqual(caseinfo['assert'], result['msg'])

    @allure.title('制单审核通过')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_doApproval.yml'))
    def test_doApproval(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        caseinfo['requests']['data']['creditNo'] = YamlUtil().read_yaml('creditNo')
        caseinfo['requests']['data']['oaIds'] = YamlUtil().read_yaml('oaid')
        data=caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, json=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual(caseinfo['assert'], result['msg'])

    @allure.title('初审、复核、终审审核通过')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('ble_reviewPassedBatch.yml'))
    def test_reviewPassedBatch(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        caseinfo['requests']['data'][0]['creditNo'] = YamlUtil().read_yaml('creditNo')
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, json=data, headers=headers)
        result = json.loads(rep)
        AssertUtil().assertEqual(caseinfo['assert'], result['msg'])


if __name__ == '__main__':
    pytest.main()