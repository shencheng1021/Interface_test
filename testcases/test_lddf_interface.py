# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 联动代发产品相关接口自动化测试
@time: 2023/10/07 11:05
"""

import time

import pytest

from common.assert_util import AssertUtil
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil
import allure

@allure.epic("接口测试")
@allure.feature("联动代发产品接口测试")
class Test_Lddf:

    @allure.title("获取可用的业务模式编号")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_busmod_query.yml'))
    def test_busmod_query_01(self,caseinfo):
        '''
        description:获取可用的业务模式编号
        '''
        result=RequestsUtil().lddf_request(caseinfo)
        YamlUtil().write_yaml({'busMod': result['data'][0]['busMod']})
        AssertUtil().assertEqual('00001',result['data'][0]['busMod'])
        AssertUtil().assertEqual('TN2022011200000606', result['data'][0]['supplierCode'])
        #assert result['data'][0]['busMod'] == '00001'
        #assert result['data'][0]['supplierCode'] == 'TN2022011200000607'

    @allure.title("查询可经办业务的账号")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_busmod_acctQuery.yml'))
    def test_busmod_acctQuery_02(self,caseinfo):
        '''
        description:查询可经办业务的账号
        '''
        caseinfo['requests']['data']['busMod']=YamlUtil().read_yaml('busMod')
        result=RequestsUtil().lddf_request(caseinfo)
        YamlUtil().write_yaml({'bbkCode':result['data'][0]['bbkCode'],'acct':result['data'][0]['bankAcct']})
        AssertUtil().assertEqual('75',result['data'][0]['bbkCode'])
        AssertUtil().assertEqual('755915678710501',result['data'][0]['bankAcct'])
        AssertUtil().assertEqual('企业网银新20161077',result['data'][0]['bankAcctName'])
        # assert result['data'][0]['bbkCode'] == '75'
        # assert result['data'][0]['bankAcct'] == '755915678710501'
        # assert result['data'][0]['bankAcctName'] == '企业网银新20161077'

    @allure.title("查询授权账号列表")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_busmod_authAcctQuery.yml'))
    def test_busmod_authAcctQuery_03(self,caseinfo):
        '''
        description:查询授权账号(搅拌站关联的物流公司账号)列表
        '''
        caseinfo['requests']['data']['bbkCode'] = YamlUtil().read_yaml('bbkCode')
        caseinfo['requests']['data']['acct'] = YamlUtil().read_yaml('acct')
        result = RequestsUtil().lddf_request(caseinfo)
        YamlUtil().write_yaml({'authAcct':result['data'][0]['authAcct']})
        AssertUtil().assertEqual('操作成功',result['msg'])
        AssertUtil().assertEqual(200,result['code'])
        AssertUtil().assertEqual('755915678710606',result['data'][0]['authAcct'])
        # assert result['msg'] == '操作成功'
        # assert result['code'] == 200
        # assert result['data'][0]['authAcct'] == '755915678710606'

    @allure.title("查询搅拌站与物流已签订的协议信息")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_busmod_agreementQuery.yml'))
    def test_busmod_agreementQuery_04(self,caseinfo):
        '''
        description:查询搅拌站与物流已签订的协议信息
        '''
        caseinfo['requests']['data']['bbkCode'] = YamlUtil().read_yaml('bbkCode')
        caseinfo['requests']['data']['acct'] = YamlUtil().read_yaml('acct')
        caseinfo['requests']['data']['authAcct'] = YamlUtil().read_yaml('authAcct')
        result = RequestsUtil().lddf_request(caseinfo)
        AssertUtil().assertEqual("操作成功",result['msg'])
        AssertUtil().assertEqual(200,result['code'])
        AssertUtil().assertEqual('TN2022011200000607',result['data'][0]['supplierCode'])
        # assert result['msg'] == "操作成功"
        # assert result['code'] == 200
        # assert result['data'][0]['supplierCode'] == 'TN2022011200000607'

    @allure.title("联动代发经办发起")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_apply.yml'))
    def test_apply_05(self,caseinfo):
        '''
        description:联动代发经办发起
        '''
        caseinfo['requests']['data']['bbkCode'] = YamlUtil().read_yaml('bbkCode')
        caseinfo['requests']['data']['acct'] = YamlUtil().read_yaml('acct')
        caseinfo['requests']['data']['authAcct'] = YamlUtil().read_yaml('authAcct')
        caseinfo['requests']['data']['expectDate'] = time.strftime('%Y%m%d',time.localtime(time.time()))
        result = RequestsUtil().lddf_request(caseinfo)
        YamlUtil().write_yaml({'txnNo': result['data']['txnNo']})
        AssertUtil().assertEqual('经办发起完成',result['msg'])
        # assert result['msg'] == '经办发起完成'
        # assert result['code'] == 200
        # assert 'txnNo' in result['data']
        # assert 'reqCode' in result['data']
        # assert 'reqStat' in result['data']

    @allure.title("联动代发经办状态查询")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_applyInfo_query.yml'))
    def test_applyInfo_query_06(self,caseinfo):
        '''
        description:联动代发经办状态查询
        '''
        caseinfo['requests']['data']['startDate'] = time.strftime('%Y%m%d',time.localtime(time.time()))
        caseinfo['requests']['data']['endDate'] = time.strftime('%Y%m%d', time.localtime(time.time()))
        result = RequestsUtil().lddf_request(caseinfo)
        i=len(result['data'])
        txnNO=YamlUtil().read_yaml('txnNo')
        flag=False
        for i in range(0,i):
            if result['data'][i]['txnNo'] == txnNO:
                YamlUtil().write_yaml({'reqCode':result['data'][i]['reqCode']})
                flag = True
        AssertUtil().assertEqual(True,flag)
        #assert flag == True

    @allure.title("联动代发经办明细查询")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('lddf_applyDetailInfo_query.yml'))
    def test_applyDetailInfo_query_07(self,caseinfo):
        '''
        description:联动代发经办明细查询
        '''
        caseinfo['requests']['data']['reqCode'] = YamlUtil().read_yaml('reqCode')
        caseinfo['requests']['data']['txnNo'] = YamlUtil().read_yaml('txnNo')
        result = RequestsUtil().lddf_request(caseinfo)
        AssertUtil().assertEqual(YamlUtil().read_yaml('txnNo'),result['data'][0]['txnNo'])
        # assert result['msg'] == '查询完成'
        # assert result['code'] == 200
        # assert result['data'][0]['txnNo'] == YamlUtil().read_yaml('txnNo')


if __name__ == '__main__':
    pytest.main()




