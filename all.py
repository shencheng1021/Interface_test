# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 执行测试脚本
@time: 2022/4/13 9:34
"""
import os

import pytest

from common.config import ConfigParser

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate temp -o reports --clean')