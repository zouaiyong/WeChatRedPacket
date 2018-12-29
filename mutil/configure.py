# -*- coding: utf-8 -*-
# @Time : 2018/8/6 15:20
# @Author : sunlin
# @File : configure.py
# @Software: PyCharm
import configparser
import json
import os

class configpy():
    def __init__(self):
        self.dir_work = os.path.dirname(os.path.abspath(__file__))
        self.config_path = self.dir_work + os.sep + 'config.ini'
        self.config_obj = configparser.ConfigParser(allow_no_value=True, delimiters='=')
    def getConfig(self,section, key):

        self.config_obj.read(self.config_path,encoding='utf-8')
        value = self.config_obj.get(section, key)
        return value

    def setConfig(self,section, key,value):
        self.config_obj.read(self.config_path,encoding='utf-8')
        self.config_obj.set(section, key,value)
        self.config_obj.update()
        with open(self.config_path, "w+",encoding='utf-8') as f:
            self.config_obj.write(f)


if __name__ == '__main__':
    con=configpy()
    print(con.setConfig('user', 'user',json.dumps({'num':'1234','statue':'2'})))
    print(con.getConfig('user','user'))
