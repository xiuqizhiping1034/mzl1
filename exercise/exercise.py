#########################################################

#
#
# 五角星代码


"""
import turtle
spiral = turtle.Turtle ()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()



"""
# import  turtle
# count = 1
# while count <= 5:
#     turtle.forward(200)
#     turtle.right(144)
#     count +=1




########################################################


#######################################################


#
#
# # 几何图形代码
#
#

# import turtle
# painter = turtle.Turtle ()
#
# painter.pencolor("blue")
#
# for i in range(50):
#     painter.forward(50)
#     painter.left(123)
#
# painter.pencolor("red")
#
# for i in range(50):
#     painter.forward(50)
#     painter.left(123)
#
# turtle.done()
#
# #########################################################


#
# ##########################################################
#
#
#
# # 复杂图形

# import turtle
#
# ninja = turtle.Turtle ()
#
# ninja.speed(10)
#
# for i in range(180):
#     ninja.forward(100)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)
#
#     ninja.penup()
#     ninja.setposition(0,0)
#     ninja.pendown()
#
#     ninja.right(2)
#
# turtle.done()

# # #########################################################
# #####
# import turtle
# turtle.speed("fastest")
# turtle.pensize(1)
# for y in range(200):
# 	turtle.forward(3 * y)
# 	turtle.left(20)
# 	turtle.right(175)






# x,y=1,2
# x,y=y,x
# print(x,y)


# import random
# lottery1 = random.randint(0,99)
# guess = eval (input("please enter your lottery (two digits )"))
#
# lotteryDight1 = lottery1 //10
# lotteryDight2 = lottery1 %10
#
#
# guessDight1 = guess //10
# guessDight2 = guess %10
#
# print("The lotteryDight1 number is ",lotteryDight1)
# print("The lotteryDight2 number is ",lotteryDight2)
# print("The guessDight1 number is ",guessDight1)
# print("The guessDight2 number is ",guessDight2)
# print("The lottery number is ",lottery1)
#
# if guess == lottery1:
#     print("congratulation you! you win 10,000 ")
# el  print("congratulation you! you win 3000 ")
# # elif((lotteryDight1 == guessDight2) or (lotteryDight1 == guessDight1) or (lotteryDight2 == guessDight2) or (lotteryDight2 == guessDight1)):
# #     print("congratulation you! you win 1000 ")
# # else:
# #     print("sorry no match ")if(lotteryDight1 == guessDight2 and lotteryDight2 == guessDight1):
#

# def ONlogN(num1, num2):
# 	total = 0
# 	j = 0
# 	for i in range(num1):
# 		while(j < num2):
# 			total += i + j
# 			j = j*2
# 	return total
# # def O1(num):
# # 	i = num
# # 	j = num*2
# # 	return i+j
#
#
# if __name__ == '__main__':
#     a = ONlogN(2,3)
#     print(a)



import pymssql
import numpy as np
#
# class SqlServer:
#     def __init__(self, host, user, pwd, db):
#         self.host = host  # 主机名
#         self.user = user  # 用户名
#         self.pwd = pwd  # 密码
#         self.db = db  # 数据库名
#
#     def __GetConnect(self):
#         if not self.db:
#             raise (NameError, "没有设置数据库信息")
#         # 连接数据库
#         self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="UTF-8")
#         cur = self.conn.cursor()
#         if not cur:
#             raise (NameError, "连接数据库失败")
#         else:
#             return cur
#
#     def ExecQuery(self, sql):  # 执行查询语句
#         cur = self.__GetConnect()
#         cur.execute(sql)
#         data = cur.fetchall()  # 一次获取全部数据
#         # 查询完毕后必须关闭连接
#         self.conn.close()
#         return data
#
# def main():
#     # 使用sa登录，密码为自设sa登录密码
#     ss = SqlServer(host="127.0.0.1:1433", user="sa", pwd="8520", db="201811101034")
#
#     data1 = ss.ExecQuery('SELECT *  FROM orders$')
#
#     # np.set_printoptions(threshold=np.inf)
#     for i in range(0, 5):
#         print(data1[i])
#
#
# if __name__ == '__main__':
#     main()

#
# import pymssql
# import numpy as np

# class SqlServer:
#     def __init__(self, host, user, pwd, db):
#         self.host = host  # 主机名
#         self.user = user  # 用户名
#         self.pwd = pwd  # 密码
#         self.db = db  # 数据库名
#
#     def __GetConnect(self):
#         if not self.db:
#             raise (NameError, "没有设置数据库信息")
#         # 连接数据库
#         self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="UTF-8")
#         cur = self.conn.cursor()
#         if not cur:
#             raise (NameError, "连接数据库失败")
#         else:
#             return cur
#
#     def ExecQuery(self, sql):  # 执行查询语句
#         cur = self.__GetConnect()
#         cur.execute(sql)
#         data = cur.fetchall()  # 一次获取全部数据
#         # 查询完毕后必须关闭连接
#         self.conn.close()
#         return data


import pymssql
import numpy as np

def main():
    connect1 = pymssql.connect(host='DESKTOP-P7IHUSA', user='sa', password='8520', database='201811101034',
                               charset='utf8')
    if connect1:
        print("OnRet连接成功")
    cursor1 = connect1.cursor()
    cursor1.execute("SELECT * FROM orders$")
    data = cursor1.fetchall()
    for i in data[:5]:
        print(i)
    cursor1.close()

if __name__ == '__main__':
    main()