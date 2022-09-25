"""
                作者 马增龙
                时间 2019.8.20
                功能
                        1)绘画出五角星
                        2)实现五角星的重叠绘制
                版本号 2.0
"""
import turtle

def draw_pentagram(size):
    """
        绘制五角星
    """
    # 计数器
    count = 1;
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """"
    主函数
    """
    # 绘制多个重叠五角星

    # 对绘画笔进行一些调整 颜色 粗度 初始位置
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')


    # # 初始长度
    size = 100
    while size <= 150:
        draw_pentagram(size)
        size += 10
    # 点击关闭
    turtle.exitonclick()

    """"
    直接调用主函数
    """

if  __name__  =='__main__':
    main()

    #    向左边画五角星
    # while count <= 5:
    #     turtle.backward(200)
    #     turtle.left(144)
    #     count += 1

    # # 绘制多个重叠五角星
    # #  初始长度
    # size = 100
    # for i in range(3):
    #
    #     for j in range(5):
    #         turtle.forward(size)
    #         turtle.right(144)
    #     size +=100
