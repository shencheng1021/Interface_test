# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 联动代发产品相关接口自动化测试
@time: 2023/10/07 11:05
"""
import json
import time

import pytest

from common.get_sign_util import GetSignUtil
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil


class Test_Lddf:

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('lddf_busmod_query.yml'))
    def test_busmod_query(self,caseinfo):
        '''
        description:获取可用的业务模式编号
        '''
        data = caseinfo['requests']['data']
        sign=GetSignUtil().get_sign(data)
        caseinfo['requests']['headers']['sign']=sign
        url=caseinfo['requests']['url']
        method=caseinfo['requests']['method']
        headers=caseinfo['requests']['headers']
        result=RequestsUtil().send_request(method,url,headers=headers,json=data)
        result=json.loads(result)
        YamlUtil().write_yaml({'busMod': result['data'][0]['busMod']})
        print(result)
        assert result['data'][0]['busMod'] == '00001'
        assert result['data'][0]['supplierCode'] == 'TN2022011200000607'

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('lddf_busmod_acctQuery.yml'))
    def test_busmod_acctQuery(self,caseinfo):
        '''
        description:查询可经办业务的账号
        '''
        caseinfo['requests']['data']['busMod']=YamlUtil().read_yaml('busMod')
        data = caseinfo['requests']['data']
        sign = GetSignUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        YamlUtil().write_yaml({'bbkCode':result['data'][0]['bbkCode'],'acct':result['data'][0]['bankAcct']})
        assert result['data'][0]['bbkCode'] == '75'
        assert result['data'][0]['bankAcct'] == '755915678710501'
        assert result['data'][0]['bankAcctName'] == '企业网银新20161077'

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('lddf_busmod_authAcctQuery.yml'))
    def test_busmod_authAcctQuery(self,caseinfo):
        '''
        description:查询授权账号(搅拌站关联的物流公司账号)列表
        '''
        caseinfo['requests']['data']['bbkCode'] = YamlUtil().read_yaml('bbkCode')
        caseinfo['requests']['data']['acct'] = YamlUtil().read_yaml('acct')
        data = caseinfo['requests']['data']
        sign = GetSignUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        YamlUtil().write_yaml({'authAcct':result['data'][0]['authAcct']})
        assert result['msg'] == '操作成功'
        assert result['code'] == 200
        assert result['data'][0]['authAcct'] == '755915678710606'

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('lddf_apply.yml'))
    def test_apply(self,caseinfo):
        '''
        description:联动代发经办发起
        '''
        caseinfo['requests']['data']['bbkCode'] = YamlUtil().read_yaml('bbkCode')
        caseinfo['requests']['data']['acct'] = YamlUtil().read_yaml('acct')
        caseinfo['requests']['data']['authAcct'] = YamlUtil().read_yaml('authAcct')
        caseinfo['requests']['data']['expectDate'] = time.strftime('%Y%m%d',time.localtime(time.time()))
        data = caseinfo['requests']['data']
        sign = GetSignUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        YamlUtil().write_yaml({'txnNo': result['data']['txnNo']})
        print(result['data']['txnNo'])
        assert result['msg'] == '经办发起完成'
        assert result['code'] == 200
        assert 'txnNo' in result['data']
        assert 'reqCode' in result['data']
        assert 'reqStat' in result['data']

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('lddf_applyInfo_query.yml'))
    def test_applyInfo_query(self,caseinfo):
        '''
        description:联动代发经办状态查询
        '''
        caseinfo['requests']['data']['startDate'] = time.strftime('%Y%m%d',time.localtime(time.time()))
        caseinfo['requests']['data']['endDate'] = time.strftime('%Y%m%d', time.localtime(time.time()))
        data=caseinfo['requests']['data']
        sign = GetSignUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        i=len(result['data'])
        flag=False
        for i in range(0,i):
            if result['data'][i]['txnNo'] == YamlUtil().read_yaml('txnNo'):
                YamlUtil().write_yaml({'reqCode':result['data'][i]['reqCode']})
                flag = True
        assert flag == True

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('lddf_applyDetailInfo_query.yml'))
    def test_applyDetailInfo_query(self,caseinfo):
        '''
        description:联动代发经办明细查询
        '''
        caseinfo['requests']['data']['reqCode'] = YamlUtil().read_yaml('reqCode')
        caseinfo['requests']['data']['txnNo'] = YamlUtil().read_yaml('txnNo')
        data = caseinfo['requests']['data']
        sign = GetSignUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        assert result['msg'] == '查询完成'
        assert result['code'] == 200
        assert result['data'][0]['txnNo'] == YamlUtil().read_yaml('txnNo')



if __name__ == '__main__':
    pytest.main()




