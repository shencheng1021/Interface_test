# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 读取yaml文件
@time: 2022/4/13 9:34
"""
import os
import yaml


class YamlUtil:

    #读取extract.yml文件
    def read_yaml(self,key):
        with open(os.path.dirname(__file__).split('common')[0]+'extract.yml',mode='r',encoding='utf-8') as file:
            value=yaml.load(stream=file,Loader=yaml.FullLoader)
            return value[key]

    def write_yaml(self,data):
        with open(os.path.dirname(__file__).split('common')[0]+'extract.yml',mode='a',encoding='utf-8') as file:
            yaml.dump(data=data,stream=file,allow_unicode=True)

    def clear_yaml(self):
        with open(os.path.dirname(__file__).split('common')[0]+'extract.yml',mode='w',encoding='utf-8') as file:
            file.truncate()


    #读取测试用例
    def read_testcase_yaml(self,filename):
        with open(os.path.dirname(__file__).split('common')[0]+'/testcases/'+filename,mode='r',encoding='utf-8') as file:
            value=yaml.load(stream=file,Loader=yaml.FullLoader)
            return value


if __name__ == '__main__':
    text=YamlUtil().read_testcase_yaml('get_token.yml')
    text[0]['request']['data']['accessToken']='233233'
    print(text)