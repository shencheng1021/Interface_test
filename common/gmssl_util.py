# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import json
import logging

import requests
from common.config import ConfigParser
from common.logger_util import Logger
from common.yaml_util import YamlUtil
import allure

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class GmSsl:

    @allure.step("对接口返回的密文进行解密")
    def gmssh_decode(self,data):
        log.logger.info('请求解密接口开始，解密数据为：%s' % data)
        url = "http://172.24.100.74:9921/decrypt"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "172.24.100.74:9921"
        }
        data='srcBody='+data
        rep = requests.request("post", url=url,data=data, headers=headers)
        log.logger.info("解密结果为：%s" % rep.json())
        return rep.json()


    @allure.step("对数据进行加密")
    def gmssh_encrypt(self,data):
        data=json.dumps(data)
        log.logger.info('请求加密接口开始，加密数据为：%s' % str(data))
        url='http://172.24.100.74:9921/encrypt'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "172.24.100.74:9921"
        }
        data='bodystr='+data
        rep = requests.request("post",url=url,data=data,headers=headers)
        log.logger.info('加密结果为：%s' % rep.json())
        return rep.json()

    @allure.step("获取解密报文中的token，并将token保存到指定yaml文件中")
    def set_token(self,key,data):
        head=GmSsl().gmssh_decode(data)
        token=head['token']
        YamlUtil().write_yaml({'token_'+key: token})

        #ConfigParser().cset('interfacetoken','token','interface_config',token)





if __name__ == '__main__':
    data='{"traderNo":"TN2022022600001213","accessToken":"98e8f243-df00-44b5-a321-8370a14d260a","userId":"13475475547","userinfo":"1700698508703","token":"eyJ1c2VySWQiOiIxMzQ3NTQ3NTU0NyIsInRva2VuIjoiN2M3NGQ4ZGZlYzkyNGZkYjg2NDkyNmVjZjYxMTU4ODkifQ==","traderName":"核心企业新1"}'
    GmSsl().gmssh_encrypt(data)