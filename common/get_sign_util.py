# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 参数加密获取headers中的sign参数
@time: 2023/10/7 14:20
"""
import json

from common.requests_util import RequestsUtil


class GetSignUtil:
    def get_sign(self,data):
        url='http://172.24.100.75:9203/expose/lddf/encrypt'
        result=RequestsUtil().send_request('post',url,json=data)
        result=json.loads(result)
        sign=result['msg']
        return sign


