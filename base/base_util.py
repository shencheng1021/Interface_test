# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging
import unittest

from common.logger_util import Logger

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)


class BaseUtil:

    def setup_method(self) -> None:
        log.logger.info('************************starting run test cases************************')

    def teardown_method(self) -> None:
        log.logger.info('************************test case run completed************************')
