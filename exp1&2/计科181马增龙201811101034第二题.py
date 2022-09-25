"""
                作者计科181 马增龙
                学号 201811101034
                时间 2020.9.25
                功能
                        1)显示一个三角形状的乘法口诀表
                        2)利用嵌套循环 控制输出
"""

print("Multiplication Table ")

#
print()
for i in range(1,10):
    for j in range (1,i+1):
         print("{}×{}={}".format(i,j,i*j), "", end=" ")
         # print("%dx%d=%d\t" % (i, j, i * j), end="")
    print()

