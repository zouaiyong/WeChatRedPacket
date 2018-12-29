import argparse
import csv
import json
import re
import unittest

import xlrd

from case import redPacketCase
from mutil import configure
from mutil.configure import configpy


def execute():
    className = redPacketCase
    suite = unittest.TestLoader().loadTestsFromName('redPacketCase',className)
    unittest.TextTestRunner(verbosity=1).run(suite)

def readexcel(path):
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

def readCsvfile(filepath):
    with open(filepath,encoding='utf-8') as file:
        f_csv=csv.DictReader(file)
        alluser = []
        for row in f_csv:
            print(row.get('电话号码'), row.get('状态'))
            user = {}
            user['phonenume'] = row.get('电话号码').strip()
            user['money'] = row.get('金额').strip()
            user['status'] = row.get('状态').strip()
            alluser.append(user)
            # conf = configpy()
            # conf.setConfig('user', 'user', json.dumps(user,ensure_ascii=False))
    return alluser

def writeCsvfile(filepath,rows):
    with open(filepath,encoding='utf-8') as file:
        f_csv = csv.DictWriter(file)
        f_csv.writerows(rows)

if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str)
    parser.add_argument("--password", type=int)
    args = parser.parse_args()
    filepath = args.filepath
    password = args.password
    alluser = readCsvfile(filepath)
    conf=configpy()
    conf.setConfig('user','password',str(password))
    if args.filepath  and  args.password:
        if alluser:
            for user in alluser:
                conf.setConfig('user', 'user', json.dumps(user, ensure_ascii=False))
                execute()
    else:
        print('''请输入正确的参数
        --filepath： type string  excel路径
        --password： type int 微信支付密码
        usage : python runcase.py --filepath D:/xxx.xlsx --password  123456''')
    #readCsvfile('提现.csv')
