# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: conftest共享文件
@time: 2022/4/13 9:34
"""
import logging

import pytest

from common.logger_util import Logger
from common.yaml_util import YamlUtil
import allure

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.step("初始化extract_yaml文件")
@pytest.fixture(scope='session',autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_yaml()





