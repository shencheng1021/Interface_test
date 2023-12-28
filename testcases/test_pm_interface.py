#-*-coding:utf-8-*-

"""
@author: shencheng
@software: PyCharm
@description: 精准营销客户邀请接口测试
@time: 2022/4/13 9:34
"""
import json

import allure
import pytest

from common.assert_util import AssertUtil
from common.excel_util import ExcelUtil
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil

@allure.feature('精准营销接口测试')
@pytest.mark.usefixtures('pm_initialization')
class TestPm:

    @allure.title('精准营销客户邀请接口测试')
    @pytest.mark.parametrize('casedata',ExcelUtil().excel_read('pm_phone'))
    def test_saveInviteRecords(self,casedata):
        RequestsUtil().send_code(str(casedata[1]))
        caseinfo=YamlUtil().read_testcase_yaml('pm_saveInviteRecords.yml')[0]
        url=caseinfo['requests']['url']
        method=caseinfo['requests']['method']
        headers=caseinfo['requests']['headers']
        caseinfo['requests']['data']['phone']=str(casedata[1])
        data=json.dumps(caseinfo['requests']['data'])
        rep=RequestsUtil().send_request(method,url,headers=headers,data=data)
        result = json.loads(rep)
        AssertUtil().assertEqual(casedata[2],result['msg'])



if __name__ == '__main__':
    pytest.main()
