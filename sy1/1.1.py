# -*- codeing = UTF-8 -*-
# @Time : 2021/5/25 15:03
# @Author : 马增龙 15634099385
# @File : 1.1.py
# @Software : PyCharm
import pandas as pd					# ①导入pandas库
pd.set_option('display.width',None)
#
# data = pd.read_csv('orders.txt',header='infer',skiprows=1,nrows=5)
# print(data)

pd.set_option('display.width', None)
data = pd.read_csv('orders.xls',header='infer',skiprows=1,nrows=5)
print(data)