# -*- codeing = UTF-8 -*-
# @Time : 2020/11/21 16:41
# @Author : 马增龙 15634099385
# @File : demo1.py
# @Software : PyCharm



# 格式化输出
age = 10
# 使用%d  和 %s  来代替后边的变量或者字符
print("我的年龄是：%d 岁"%age)

print("我的名字是%s,我的国籍是%s"%("小张","中国"))
# 前边有多个站位的话 用括号引起来 一个%即可

print('dsak','sdokfs','dlkosa')
print('www','baidu','com',sep='.')
#使用sep可以来将字符串进行分隔开
print("hello",end='')
print('world',end='\t')
print('python',end='\n')

password = input('请输入密码:')
print('您输入的密码是：',password)

#type(变量名称) 用来测试变量的类型
a = input('请输入')
print(type(a))

#python 也可以直接使用类型强制转换
b = int("123")

