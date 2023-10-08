# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 提出requests方案，修改为独立的公用模块，后续接口请求统一调此方案
@time: 2022/4/13 9:34
"""
import json

import requests
import allure


class RequestsUtil:

    session = requests.session()

    @allure.step("初始化request方法")
    def send_request(self,method,url,**kwargs):
        rep=RequestsUtil.session.request(method,url=url,**kwargs)
        return rep.text


    @allure.step("获取联动代发产品请求header中的sign")
    def get_sign(self,data):
        url='http://172.24.100.75:9203/expose/lddf/encrypt'
        result=RequestsUtil().send_request('post',url,json=data)
        result=json.loads(result)
        sign=result['msg']
        return sign

    @allure.step("获取请求联动代发产品请求的url、method、headers、data并执行")
    def lddf_request(self, caseinfo):
        data = caseinfo['requests']['data']
        sign = RequestsUtil().get_sign(data)
        caseinfo['requests']['headers']['sign'] = sign
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        headers = caseinfo['requests']['headers']
        result = RequestsUtil().send_request(method, url, headers=headers, json=data)
        result = json.loads(result)
        return result
