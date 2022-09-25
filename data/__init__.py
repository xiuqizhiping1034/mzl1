# -*- codeing = UTF-8 -*-
# @Time : 2021/3/21 20:44
# @Author : 马增龙 15634099385
# @File : __init__.py.py
# @Software : PyCharm

#
#
#
# import  pandas as pd
#
# pd.set_option('display.width',None)
# data = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\最新白马股.csv',sep=',',header=0).head(5)
# print(data)
#
# print("******************************************************************************")
# print("******************************************************************************")
# print("******************************************************************************")
# pd.set_option('display.width',None)
# data = pd.read_excel('C:\\Users\\Lenovo\\Desktop\\最新白马股.xlsx',header=0).head(5)
# print(data)


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# df=pd.read_csv('C:\\Users\\Lenovo\\Desktop\\Stock_Analysis.csv',encoding='GBK')
# plt.scatter(df[' 每股净资产'], df[' 净资产收益率'],marker='s',c='red')
# plt.rcParams['font.sans-serif']=['SimHei'] # 显示中文标签
# plt.rcParams['axes.unicode_minus']=False # 这两行需要手动设置
# plt.title("Scatter")
# plt.xlabel(' 每股净资产')
# plt.ylabel(' 净资产收益率')
# plt.show()
#





# coding: utf-8

import turtle as t


def main():
    """
    画小猪佩奇的身体
    :return: null
    """
    t.color((255, 99, 71), "red")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-78)
    t.pd()
    t.begin_fill()
    t.seth(-130)
    t.circle(100, 10)
    t.circle(300, 30)
    t.seth(0)
    t.fd(230)
    t.seth(90)
    t.circle(300, 30)
    t.circle(100, 3)
    t.color((255, 155, 192), (255, 100, 100))
    t.seth(-135)
    t.circle(-80, 63)
    t.circle(-150, 24)
    t.end_fill()
    # draw_Eight_Diagrams()
    # 允许用户自己点击关闭
    t.exitonclick()


if  __name__  =='__main__':
    main()

