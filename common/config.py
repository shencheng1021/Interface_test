# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import configparser

#获取指定键
class ConfigParser:
    def cget(self,section,options,filename):
        cp=configparser.ConfigParser()
        with open('../config_file/'+filename+'.ini') as f:
            cp.read_file(f)
            a=cp.get(section,options)
        return a

    #设置指定键
    def cset(self,section,options,filename,value):
        cp=configparser.ConfigParser()
        with open('../config_file/'+filename+'.ini') as f:
            cp.read_file(f)
            cp.set(section,options,value)
        with open('../config_file/'+filename+'.ini','w') as f:
            cp.write(f)

    #获取section下的所以键
    def cget_section(self,section,options,filename):
        cp=configparser.ConfigParser()
        with open('../config_file/'+filename+'.ini') as f:
            cp.read_file(f)
            data=cp.items(section)
            return dict(data)

if __name__ == '__main__':
    print(ConfigParser().cget('interfacetoken','token','interface_config'))
