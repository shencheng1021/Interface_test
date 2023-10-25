# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 提出requests方案，修改为独立的公用模块，后续接口请求统一调此方案
@time: 2022/4/13 9:34
"""
import json
import logging

import requests
import allure

from common.logger_util import Logger

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class RequestsUtil:

    session = requests.session()

    @allure.step("初始化request方法")
    def send_request(self,method,url,**kwargs):
        log.logger.info("请求地址:%s" % str(url))
        log.logger.info("请求方式:%s" % str(method))
        try:
            rep=RequestsUtil.session.request(method,url=url,**kwargs)
        except Exception as e:
            log.logger.exception("接口请求失败",exc_info=True)
            raise e
        else:
            log.logger.info("请求结果状态码：[%s]" % rep.status_code)
            log.logger.info("响应结果：%s" % str(rep.text))
            return rep.text


    @allure.step("获取联动代发产品请求header中的sign")
    def get_sign(self,data):
        url='http://172.24.100.75:9203/expose/lddf/encrypt'
        try:
            result = RequestsUtil().send_request('post',url,json=data)
            result = json.loads(result)
            sign = result['msg']
        except Exception as e:
            log.logger.exception("sign获取失败",exc_info=True)
            raise e
        else:
            log.logger.info("sign值：%s" % sign)
            return sign

    @allure.step("获取请求联动代发产品请求的url、method、headers、data并执行")
    def lddf_request(self, caseinfo):
        data = caseinfo['requests']['data']
        sign = RequestsUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        log.logger.info("请求头:%s" % str(headers))
        log.logger.info("data:%s" % str(data))
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        return result
