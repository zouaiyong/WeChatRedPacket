# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:22
# @Author  : zouay
# @Email   : zouaiyong@tuandai.com
# @File    : redPacketCase.py
# @Software: PyCharm
import os
import unittest
from time import sleep

import mutil.TestCaseUtil

class redPacketCase(mutil.TestCaseUtil.TestCaseUtil):
    def caseExecute(self):



        id=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ij")')
        id.click()
        #sleep(2)
        textid=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/ka")')
        textid.click()
        textid.clear()
        inputtext='大抠B'
        adbcommond='adb shell am broadcast -a ADB_INPUT_TEXT --es msg {inputtext}'.format(inputtext=inputtext)
        os.system(adbcommond)
        #sleep(3)
        alias=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/pp")')
        alias.click()
        #sleep(5)
        chat=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/alr")')
        chat.click()
        #sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Red Packet")').click()
        #sleep(2)
        #rednum=self.driver.find_element_by_android_uiautomator('new UiSelector().text("0.00")')
        rednum=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/csk")')
        #rednum=self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.tencent.mm:id/csk"]')

        rednum.clear()
        self.driver.set_value(rednum,'0.1')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/cuj")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/f5s")').click()
        password = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tencent.mm:id/ccm")')
        password.click()
        self.driver.set_value(password, '200888')




    pass

if __name__ == '__main__':
    #className=sys.argv[0].split('.')[0]
   #print("------------",className)
    suite=unittest.TestLoader().loadTestsFromTestCase(redPacketCase)
    #suite = unittest.TestLoader().loadTestsFromName(redPacketCase.redPacketCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
    pass