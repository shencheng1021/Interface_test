#-*-coding:utf-8-*-

"""
@author: shencheng
@software: PyCharm
@description: 读取yaml文件
@time: 2022/4/13 9:34
"""
import logging
import os
import yaml

from common.logger_util import Logger

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)


class YamlUtil:

    #读取extract.yml文件
    def read_yaml(self,key):
        log.logger.info("读取extract.yml文件中key为: %s 的数据" % key)
        try:
            with open(os.path.dirname(__file__).split('common')[0]+'extract.yml',mode='r',encoding='utf-8') as file:
                value=yaml.load(stream=file,Loader=yaml.FullLoader)
        except Exception as e:
            log.logger.exception("读取extract.yml文件失败",exc_info=True)
            raise e
        else:
            log.logger.info("extract.yml文件key值为：%s 的值为 %s " % (key,value[key]))
            return value[key]

    def write_yaml(self,data):
        log.logger.info("写入extract.yml文件内容: %s" % data)
        try:
            with open(os.path.dirname(__file__).split('common')[0]+'extract.yml',mode='a',encoding='utf-8') as file:
                yaml.dump(data=data,stream=file,allow_unicode=True)
        except Exception as e:
            log.logger.exception("写入extract.yml文件失败",exc_info=True)
            raise e
        else:
            log.logger.info("写入extract.yml文件成功")

    def clear_yaml(self):
        try:
            with open(os.path.dirname(__file__).split('common')[0]+'extract.yml',mode='w',encoding='utf-8') as file:
                file.truncate()
        except Exception as e:
            log.logger.exception("清除extract.yml文件内容失败", exc_info=True)
            raise e
        else:
            log.logger.info("清除extract.yml文件内容成功")


    #读取测试用例数据
    def read_testcase_yaml(self,filename):
        try:
            with open(os.path.dirname(__file__).split('common')[0]+'data/'+filename,mode='r',encoding='utf-8') as file:
                value=yaml.load(stream=file,Loader=yaml.FullLoader)
        except Exception as e:
            log.logger.exception("读取%s文件中测试用例数据失败" % filename,exc_info=True)
            raise e
        else:
            log.logger.info("读取%s文件中测试用例数据成功" % filename)
            return value



if __name__ == '__main__':
    text=YamlUtil().read_testcase_yaml('get_token.yml')
    text[0]['request']['data']['accessToken']='233233'
    print(text)