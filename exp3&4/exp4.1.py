s= eval(input())
sum = 0
while (s >0):
    sum =sum +s%10
    # s =int(s/10)# 此处需要将数据直接向下取整  变成整数之后 再相加
    s =s//10
    print(s)
print(sum)
# s= input()
# sum = 0
# for i in range (0,len(s),1):
#     sum+=eval(s[i])
# print(sum)