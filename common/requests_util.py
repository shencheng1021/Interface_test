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

from common import dir_util
from common.assert_util import AssertUtil
from common.logger_util import Logger
from common.yaml_util import YamlUtil

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class RequestsUtil:

    session = requests.session()

    @allure.step("初始化request方法")
    def send_request(self,method,url,**kwargs):
        log.logger.info("请求地址:%s" % str(url))
        log.logger.info("请求方式:%s" % str(method))
        dh=dict(**kwargs)
        for item in dh.items():
            if item[0] == 'data' or item[0] =='params' or item[0] =='json':
                log.logger.info('请求测试数据为：%s' % item[1])
            if item[0] == 'headers':
                log.logger.info('请求头为：%s' % item[1])
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


    def upload_file(self,key,filename):
        # filetype = filename.split('.')[1]
        # type=''
        # if filetype == 'pdf':
        #     type = 'application/pdf'
        # elif filetype == 'jpg':
        #     type = 'image/jpeg'
        # elif filetype == 'png':
        #     type = 'image/png'
        # elif filetype == 'xls':
        #     type = 'application/vnd.ms-excel'
        # elif filetype == 'xlsx':
        #     type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        # else:
        #     log.logger.info('上传的文件类型：%s,目前暂无法支持!')
        #     return False

        caseinfo=YamlUtil().read_testcase_yaml('TFileUploadAction.yml')[0]
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token_supplier')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        headers = caseinfo['requests']['headers']
        data = {}
        path=dir_util.dir + 'data/'
        files = [
            ('file',(filename,open(path+filename,'rb')))
        ]
        rep = RequestsUtil().send_request(method, url, headers=headers, data=data, files=files)
        result = json.loads(rep)
        YamlUtil().write_yaml({key : result['fileNo']})

    def invoice_vatBatch(self,filenamelsit,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token_supplier')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        headers = caseinfo['requests']['headers']
        data = {}
        path = dir_util.dir + 'data/'
        files = []
        index=0
        #上传多个文件时组装files文件流
        for item in filenamelsit:
            files.append('')
            files[index]=('files',(item,open(path+item,'rb')))
            index=index+1
        log.logger.info(files)
        rep = RequestsUtil().send_request(method, url, headers=headers, data=data, files=files)
        result = json.loads(rep)
        invoiceList=result['data']    #获取识别的发票列表
        #将识别的发票信息写入到extract.yml中
        YamlUtil().write_yaml({'invoiceList': invoiceList})
        # for invoice,keys in zip(invoiceList,filenamelsit):
        #     YamlUtil().write_yaml({'invoiceList': {keys: invoice['data']}})
        return result

    def upload_invoice(self,caseinfo):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token_supplier')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        headers = caseinfo['requests']['headers']
        data=[]
        invoiceList=YamlUtil().read_yaml('invoiceList')
        for inv in invoiceList:
            item_dict = {
                'invoiceNo': inv['data']['invoiceNumber'],
                'invoiceCode': inv['data']['invoiceCode'],
                'billingDate': inv['data']['billingDate'],
                'totalAmt': inv['data']['totalAmount'],
                'invoiceAmt': inv['data']['invoiceAmount'],
                'taxAmt': inv['data']['taxAmount'],
                'invoiceImage': inv['data']['fileNo'],
                'fileNo': inv['data']['fileNo'],
                'checkCode': inv['data']['checkCode'],
                'invoiceType': inv['data']['invoiceType'],
                'creditNo': YamlUtil().read_yaml('creditNo'),
                'fileName': inv['data']['title'],
                'revAmt': inv['data']['title'],
                'checkStatus': '1'
                }
            data.append(item_dict)
        rep=RequestsUtil().send_request(method,url,headers=headers,json=data)
        resulit=json.loads(rep)
        return resulit

    def revAmt_update(self,caseinfo,fileNO,revAmt):
        url = caseinfo['requests']['url']
        method = caseinfo['requests']['method']
        token = YamlUtil().read_yaml('token_supplier')
        caseinfo['requests']['headers']['Cookie'] = 'Token=' + token
        caseinfo['requests']['headers']['Token'] = token
        headers = caseinfo['requests']['headers']
        caseinfo['requests']['data']['creditNo'] = YamlUtil().read_yaml('creditNo')
        caseinfo['requests']['data']['revAmt'] = revAmt
        caseinfo['requests']['data']['fileNo'] = fileNO
        data = caseinfo['requests']['data']
        rep = RequestsUtil().send_request(method, url, headers=headers, params=data)
        resulit = json.loads(rep)
        return resulit


if __name__ == '__main__':
    #RequestsUtil().invoice_vatBatch(['invoice01.jpg','invoice02.jpg'],YamlUtil().read_testcase_yaml('invoice_vatBatch.yml')[0])
    RequestsUtil().upload_invoice(YamlUtil().read_testcase_yaml('ble_upload_invoice.yml')[0])
    #RequestsUtil().revAmt_update('b6229fa3b1f14b3cb517d7b7af7673b2','5000')

