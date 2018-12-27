# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:04
# @Author  : zouay
# @Email   : aiiyong.zou@outlook.com
# @File    : TestCaseUtil.py
# @Software: PyCharm
import re
import unittest
import os
import sys
from time import sleep
from appium import webdriver

class TestCaseUtil(unittest.TestCase):

    def setUp(self):
        print("set up  is run")
        deviceId ='bf5fb4a2' #sys.argv[1]
        deviceAndroidVersion = list(
            os.popen(
                'adb -s %s shell getprop ro.build.version.release' %
                deviceId).readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        print(deviceId, deviceVersion)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = deviceVersion
        desired_caps['deviceName'] = deviceId
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['noReset'] = True
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['resetKeyboard']=True
        desired_caps['unicodeKeyboard']=True
        # self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.driver.launch_app()
        sleep(3)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        print("tear down is run")

    def test_case(self):
        try:
            print('parent test case')
            self.caseExecute()

        except Exception as e:
            raise Exception("error throw", 1)

    def caseExecute(self):
        print('parent case execute')
        pass
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseUtil)
    unittest.TextTestRunner(verbosity=1).run(suite)
