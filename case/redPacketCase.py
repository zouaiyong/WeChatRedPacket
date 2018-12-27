# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:22
# @Author  : zouay
# @Email   : zouaiyong@tuandai.com
# @File    : redPacketCase.py
# @Software: PyCharm
import unittest
from time import sleep

import mutil.TestCaseUtil

class redPacketCase(mutil.TestCaseUtil.TestCaseUtil):
    def caseExecute(self):
        id=self.driver.find_element_by_id('com.tencent.mm:id/ij')
        id.click()
        sleep(1)
        textid=self.driver.find_element_by_id('com.tencent.mm:id/ka')
        textid.click()
        textid.clear()
        sleep(1)
        textid.send_keys('dadadada')


    pass

if __name__ == '__main__':
    #className=sys.argv[0].split('.')[0]
   #print("------------",className)
    suite=unittest.TestLoader().loadTestsFromTestCase(redPacketCase)
    #suite = unittest.TestLoader().loadTestsFromName(redPacketCase.redPacketCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
    pass