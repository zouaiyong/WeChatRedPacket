# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:22
# @Author  : zouay
# @Email   : zouaiyong@tuandai.com
# @File    : redPacketCase.py
# @Software: PyCharm

import argparse
import json
import os
import re
import sys
import unittest
from time import sleep

import requests
import xlrd
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append(".")
import mutil.TestCaseUtil
from mutil.configure import configpy


class sendRedPacket(mutil.TestCaseUtil.TestCaseUtil):


    def caseExecute(self):

        apiurl = 'http://nodejs999.com/api/video/v1/sendmoney2'
        params = {'id': '123', 'type': 2, 'xtype': 4}
        #password = conf.getConfig('user', 'password')
        passlist = list(str(password))
        print(passlist)
        keycodvalue = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16}

        if alldata:
            alluser = alldata.get('data').get('r1')
            for user in alluser:
                if  user.get('type')==1:
                    try:
                        self.driver.launch_app()
                        sleep(3)
                        id=self.driver.find_element_by_android_uiautomator('new UiSelector().description("Search")')
                        #id=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ij")')
                        id.click()
                        #textid=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ka")')
                        textid = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ji")')
                        textid.click()
                        textid.clear()
                        inputtext=user.get('tel')
                        print(inputtext)
                        adbcommond='adb shell am broadcast -a ADB_INPUT_TEXT --es msg {inputtext}'.format(inputtext=inputtext)
                        os.system(adbcommond)
                        alias = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/jv")')
                        #alias=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/pp")')
                        aliastext=alias.text.split(':')[1].strip()
                        print(aliastext)
                        if inputtext==aliastext:
                            alias.click()
                            #chat=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/alr")')
                            chat=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/aij")')

                            chat.click()
                            #sleep(1)
                            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Red Packet")').click()
                            #sleep(2)
                            #rednum=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/csk")')
                            rednum=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/clu")')

                            rednum.clear()
                            money=str(int(user.get('money'))/100)
                            self.driver.set_value(rednum,money)
                            self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/cnh")').click()
                            #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/cuj")').click()

                           #self.driver.find_element_by_android_uiautomator('new UiSelector().text("Password")').click()
                            #sleep(3)
                            self.driver.find_element_by_android_uiautomator(
                                'new UiSelector().resourceId("com.tencent.mm:id/c7u")').click()
                            print(keycodvalue.get(passlist[0]))
                            self.driver.press_keycode(keycodvalue.get(passlist[0]))
                            self.driver.press_keycode(keycodvalue.get(passlist[1]))
                            self.driver.press_keycode(keycodvalue.get(passlist[2]))
                            self.driver.press_keycode(keycodvalue.get(passlist[3]))
                            self.driver.press_keycode(keycodvalue.get(passlist[4]))
                            self.driver.press_keycode(keycodvalue.get(passlist[5]))
                            #sleep(1)
                            self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/alw")')
                            self.driver.back()
                            params['id'] = user.get('id')
                            requests.get(apiurl, params=params)
                        else:
                            raise Exception("error throw", '不是好友')
                    except Exception as e:
                        print(str(e))


                    self.tearDown()




if __name__ == '__main__':
    global alldata
    global password
    dataapi = 'http://nodejs999.com/api/video/v1/runquery2'

    dataparams = {'time': '', 'xtype': 4, 'time2': '', 'stype': 3, 'adtype': 3}
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", type=int)
    parser.add_argument('--startTime', type=str)
    parser.add_argument('--endTime', type=str)
    args = parser.parse_args()

    password = str(args.password)
    #conf = configpy()
    #conf.setConfig('user', 'password', str(password))
    if args.startTime and args.password and args.endTime:
        dataparams['time'] = args.startTime
        dataparams['time2'] = args.endTime
        respones = requests.get(dataapi, params=dataparams)

        alldata= respones.json()
        if alldata:
            suite=unittest.TestLoader().loadTestsFromTestCase(sendRedPacket)
            unittest.TextTestRunner(verbosity=1).run(suite)


    else:
        print('''请输入正确的参数
            --filepath： type string  excel路径
            --password： type int 微信支付密码
            --startTime:  type string 开始时间
            --endTime：  type string 结束时间
            usage : python runcase.py  --password  123456 --startTime 2019-1-11 --endTime 2019-01-12''')
