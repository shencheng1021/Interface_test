# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 获取系统路径的公共模块
@time: 2023/11/01 15:49
"""
import os
import sys

# print(os.path.dirname(sys.argv[0]))
#
# print(os.getcwd())
#
# print(os.path.abspath(os.curdir))
#
# print(os.path.abspath('.'))
#
# print(sys.path[0])
#
# print(sys.argv[0])
#
# print(os.path.abspath(__file__))
#
# print(os.path.dirname(__file__))
#
# print(os.path.realpath(__file__))

#获取系统当前路径
dir = os.path.dirname(__file__).split('common')[0]

#获取测试数据路径
testdata_dir=dir+'data/'
#测试数据路径
#datadir=dir+'data'