#-*-coding:utf-8-*-

"""
@author: shencheng
@software: PyCharm
@description: conftest共享文件
@time: 2022/4/13 9:34
"""
import logging

import pytest

from common import time_util
from common.logger_util import Logger
from common.mysql_util import MysqlConnection
from common.yaml_util import YamlUtil
import allure

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.step("初始化extract_yaml文件")
@pytest.fixture(scope='session',autouse=True)
def clear_extract_yaml():
    log.logger.info("清除extract_yaml文件内容")
    YamlUtil().clear_yaml()

@pytest.fixture(scope='function',autouse=True)
def run_test_case():
    log.logger.info('************************starting run test cases************************')
    yield
    log.logger.info('************************test case run completed************************')

@allure.step("初始化OA信息")
@pytest.fixture(scope='function',autouse=False)
def oa_information_initialization():
    date=time_util.now_date
    sql="INSERT INTO `tjf_manage01`.`t_company_financing_amount_info` (`flow_code`, `company`, " \
        "`company_code`, `sub_company`, `sub_company_busi_lice_no`, `supplier`, `supplier_busi_lic" \
        "e_no`, `amount`, `bank`, `bank_verify_status`, `bank_code`, `deleted`, `applied_date`, `a" \
        "pply_date`, `remark`, `create_time`, `update_time`) VALUES ( '345666', '海关监管和机构行家', " \
        "NULL, '核心企业新1', '511423405252476639', '供应商新101', '51142329765987177D', 10000.00, '建" \
        "设银行', 0, NULL, 0, "+date+", "+date+", '手动补充数据', NOW(), NOW());"
    MysqlConnection('tjf_manage01').Operate(sql)
    log.logger.info('*******初始化OA信息完成********')

@allure.step("初始化精准营销邀请信息")
@pytest.fixture(scope='class',autouse=False)
def pm_initialization():
    sql="DELETE FROM u_user_invite_record WHERE qr_id = 'dcaa246c98d845d4a7122664efa2ac22' AND customer_mobile = '13722220001'"
    MysqlConnection('tjf_manage01').Operate(sql)
    log.logger.info('*******初始化精准营销邀请信息完成********')






