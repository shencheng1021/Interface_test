# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import configparser

#获取指定键
import os


class ConfigParser:
    def cget(self,section,options,filename):
        cp=configparser.ConfigParser()
        with open(os.path.dirname(__file__).split('common')[0]+'/config_file/'+filename+'.ini') as f:
            cp.read_file(f)
            data=cp.get(section,options)
        return data

    #设置指定键
    def cset(self,section,options,filename,value):
        cp=configparser.ConfigParser()
        with open(os.path.dirname(__file__).split('common')[0]+'/config_file/'+filename+'.ini') as f:
            cp.read_file(f)
            cp.set(section,options,value)
        with open(os.path.dirname(__file__).split('common')[0]+'/config_file/'+filename+'.ini','w') as f:
            cp.write(f)

    #获取section下的所以键
    def cget_section(self,section,options,filename):
        cp=configparser.ConfigParser()
        with open(os.path.dirname(__file__).split('common')[0]+'/config_file/'+filename+'.ini') as f:
            cp.read_file(f)
            data=cp.items(section)
            return dict(data)


if __name__ == '__main__':

    print(os.path.dirname(__file__))
    #print(ConfigParser().cget('interfacetoken','token','interface_config'))
