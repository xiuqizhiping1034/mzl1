"""    请求网页
import  requests"""
import urllib3

urL= "http://www.baidu.com"
print("第一种方法")

respons1 = urllib3.urlopen(urL)

print(respons1.getcode())

print(len(respons1.read()))


