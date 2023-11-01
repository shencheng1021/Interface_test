# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 处理时间格式的公共类
@time: 2023/11/01 9:34
"""
import os
import time

#获取当前日期并格式化为'%Y%m%d'
now_date=time.strftime('%Y%m%d',time.localtime(time.time()))

#获取当前日期并格式化为'%Y%m%d%H%M%S'
now_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

