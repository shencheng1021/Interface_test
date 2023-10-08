# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

import requests
from common.config import ConfigParser
from common.yaml_util import YamlUtil
import allure

class GmSsl:

    @allure.step("对接口返回的密文进行解密")
    def gmssh_decode(self,data):
        url = "http://172.24.100.74:9921/decrypt"
        headers = {
            "Content-Type": "application/json",
            "Host": "172.24.100.74:9921"
        }

        rep = requests.request("post", url=url,data=data, headers=headers)
        return rep.json()

    @allure.step("获取解密报文中的token，并将token保存到指定yaml文件中")
    def set_token(self,data):
        head=GmSsl().gmssh_decode(data)
        token=head['token']
        YamlUtil().write_yaml({'token':token})

        #ConfigParser().cset('interfacetoken','token','interface_config',token)





if __name__ == '__main__':
    head='{"head":{"dgtlEnvlp":"0497a2ed84f76fa46c38e87843f15626f69066edea5da538f89204c2ee13699926be9e70a7cc0ed9b854a42fbaa01854918345ec6538003453bb6a65778509cd196dfeaa9fbe3d812fb21e277a02256cb9b6e41def8c77fad182e886da8411f5fadd6b9ee6186141876c47641fced8dac9ab2b0703c8d85b3d0ac9469c60cdc7f7","sign":"96052f105259a7f693bdfa3037d4e25bfbda7be946832e0954fddacca7c2b736"},"body":"e937cfc040b780098eed6371c0e6749a787bc280c86992023de63c6feec1d71365af2c407875b0ba947adfe179808a44f34a2f3c465286d2dd4cc8fcb62b11d1b50f35662506e5411ad23bef53e60a4c0051755a6c3c197e20fabee760cbb6b0653704f90417aa8e2c19549ded3cdc8cf80640ed15e5d43ba35b0f232a150905d122ddd976f831202e6846a4c32bf28ccdec8f6692ebcfee5c16342b65e53826a928385d808d3e2d178b63b059c033082f9c79322e1c3d77eee2dd9b769dd8edc0227fdaae68a9531d223c8d4397b197ef3ee00b43d9cc00b1d1c029037bf491e4e27c1e509995f14bc23de373cb264fe3b1cecd1b2f418cb867f4588bddf63e352720ac56196245fb135f08889ee8391491234412e7cef61bf09735a3758c96"}'
    GmSsl().set_token(head)