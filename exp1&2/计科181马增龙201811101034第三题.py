"""
                作者计科181 马增龙
                学号 201811101034
                时间 2020.9.25
                功能
                        1)实现数字金字塔
                        2)利用 for循环控制行数
                        3)利用while循环控制数字个数
                        4）注意使用format函数进行控制格式输出
"""
a = int(input('请输入层数：'))

for i in range(a):
    # 调节数字前方空格数量
    # 可针对层数为一位数、两位数的金字塔打印
    if i < 10:
        print(' '*(a - 8) + '  '*(a + 1 - i), end='')
    else:
        print('   ' * (a + 1 - i), end='')
    # 输出金字塔左半部分（包括0）
    j = i
    while j != -1:
        print(j+1, end=' ')
        j = j - 1
    # 输出金字塔右半部分（不包括0）
    j = 1
    while j != i+1:
        print(j+1, end=' ')
        j = j + 1

    print()

    # print("金字塔 ")
    #
    # p = eval(input("Enter the number :(1 to 15):"))
    # print()
    # for i in range(1,p+1):
    #
    #     for j in range (i,1,-1):
    #          print("{}".format(j),end="")
    #
    #     for j in range(1, i + 1):
    #          print("{}".format(j), "", end=" ")
    #
    #          # print("%dx%d=%d\t" % (i, j, i * j), end="")
    #     print()