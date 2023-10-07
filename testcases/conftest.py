# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: conftest共享文件
@time: 2022/4/13 9:34
"""
import pytest

from common.yaml_util import YamlUtil


@pytest.fixture(scope='function')
def con_database():
    print('连接数据库')
    yield  'wwww'
    print("关闭")

@pytest.fixture(scope='session',autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_yaml()

