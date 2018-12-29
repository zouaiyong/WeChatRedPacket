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
import unittest
from time import sleep

import xlrd

import mutil.TestCaseUtil
from mutil.configure import configpy


class redPacketCase(mutil.TestCaseUtil.TestCaseUtil):
    def caseExecute(self):
        conf = configpy()
        password=conf.getConfig('user', 'password')
        user=conf.getConfig('user','user')
        userdic=json.loads(user)
        passlist=list(password)
        keycodvalue={'0':7,'1':8,'2':9,'3':10,'4':11,'5':12,'6':13,'7':14,'8':15,'9':16}
        sleep(3)
        id=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ij")')
        id.click()
        textid=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ka")')
        textid.click()
        textid.clear()
        inputtext=userdic.get('phonenume')
        print(inputtext)
        adbcommond='adb shell am broadcast -a ADB_INPUT_TEXT --es msg {inputtext}'.format(inputtext=inputtext)
        os.system(adbcommond)
        alias=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/pp")')
        alias.click()
        chat=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/alr")')
        chat.click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Red Packet")').click()
        sleep(2)
        rednum=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/csk")')
        rednum.clear()
        money=user.get('money')
        self.driver.set_value(rednum,money)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/cuj")').click()

       #self.driver.find_element_by_android_uiautomator('new UiSelector().text("Password")').click()
        #sleep(1)
        self.driver.press_keycode(keycodvalue.get(passlist[0]))
        self.driver.press_keycode(keycodvalue.get(passlist[1]))
        self.driver.press_keycode(keycodvalue.get(passlist[2]))
        self.driver.press_keycode(keycodvalue.get(passlist[3]))
        self.driver.press_keycode(keycodvalue.get(passlist[4]))
        self.driver.press_keycode(keycodvalue.get(passlist[5]))
        sleep(2)
        self.driver.back()


    def readexcel(self,path):
        alluser = []
        try:
            excel=xlrd.open_workbook(path)
            sheet=excel.sheet_by_index(0)
            coldict={}
            for col in range(0,sheet.ncols):
                value = sheet.cell(0, col).value.strip()
                value = re.sub(r'\s', '', value)
                coldict[value] = col

            for row in range(1, sheet.nrows):
                try:
                    user={}
                    user['phonenume']=sheet.cell(row,coldict.get('电话号码')).value.strip()
                    user['money']=sheet.cell(row,coldict.get('金额')).value.strip()
                    user['status']=sheet.cell(row,coldict.get('操作')).value.strip
                    user['row']=row
                    user['col']=coldict.get('操作')
                    if '已结算' not in user.get('status'):
                        alluser.append(user)
                except Exception as e:
                    print('excel 读取行内容失败，跳过此行，继续下一行')
                    continue
        except Exception as e:
            print('excel 文件读取异常,异常信息：',str(e))
        return alluser

    pass

if __name__ == '__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(redPacketCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
    pass