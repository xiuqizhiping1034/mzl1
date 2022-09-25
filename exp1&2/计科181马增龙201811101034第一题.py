"""
                作者计科181 马增龙
                学号 201811101034
                时间 2020.9.25
                功能
                        1)实现剪刀石头布游戏
                        2)利用 random函数随机生成
                        3)使用if else控制条件
"""
import random
random1 = random.randint(0,2)
print("这是一个剪刀石头布游戏，其中0代表剪刀，1代表石头，2代表布，然后与智能对手进行比较")
input1 = eval(input("请输入数字(0/1/2)"))
print("智能对手的数字是 ",random1)
if random1 == 0:
    print("对手结果是 剪刀")
elif random1 == 1:
    print("对手结果是 石头")
else:
    print("对手结果是 布")
if random1 == input1:
    print("比赛结果是 (平局)")
elif ((random1==0 and input1 == 1) or (random1==1 and input1 == 2) or (random1==2 and input1 == 0)):
    print("恭喜你！ 你赢了")
else:
    print("再接再厉！下次一定战胜智能对手")
