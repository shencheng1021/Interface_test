# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 提出requests方案，修改为独立的公用模块，后续接口请求统一调此方案
@time: 2022/4/13 9:34
"""
import requests


class RequestsUtil:

    session = requests.session()

    def send_request(self,method,url,**kwargs):
        rep=RequestsUtil.session.request(method,url=url,**kwargs)
        return rep.text