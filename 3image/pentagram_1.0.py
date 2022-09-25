"""
                作者 马增龙
                时间 2019.8.20
                功能 绘画出五角星
                版本号 1.0
"""
import turtle

def main():
    """"
    主函数
    """

    # 计数器
    count = 1 ;
    while count <= 5:
        turtle.forward(200)
        turtle.right(144)
        count += 1
    count = 1;
    while count <= 5:
        turtle.backward(200)
        turtle.left(144)
        count += 1
    # # 第一条边
    # turtle.forward(200)
    # turtle.right(144)
    # # 第二条边
    # turtle.forward(200)
    # turtle.right(144)
    # # 第三条边
    # turtle.forward(200)
    # turtle.right(144)
    # # 第四条边
    # turtle.forward(200)
    # turtle.right(144)
    # # 第五边
    # turtle.forward(200)
    # turtle.right(144)

    # # 第一条边
    # turtle.backward(200)
    # turtle.left(144)
    # # 第二条边
    # turtle.backward(200)
    # turtle.left(144)
    # # 第三条边
    # turtle.backward(200)
    # turtle.left(144)
    # # 第四条边
    # turtle.backward(200)
    # turtle.left(144)
    # # 第五边
    # turtle.backward(200)
    # turtle.left(144)

    # 点击关闭
    turtle.exitonclick()



    """"
    直接调用主函数
    """


if  __name__  =='__main__':
    main()