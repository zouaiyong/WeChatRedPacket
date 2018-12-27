import sys
import unittest
import click

def execute():
    className = 'redPacketCase'
    print("------------", className)
    suite = unittest.TestLoader().loadTestsFromName(className + '.' + className)
    unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ =='__main__':
    execute()
    pass