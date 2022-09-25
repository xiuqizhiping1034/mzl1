"""
                作者 马增龙
                时间 2019.8.21
                功能
                    利用递归函数绘制分形树

                版本号 1.0
"""
import turtle
def draw_branch(branch_length) :
    """
    绘制分形树的函数
    """
    # 绘制右侧树枝
    if branch_length >= 5:
        if branch_length <= 15:
            turtle.color('green')
        turtle.forward(branch_length)
        print('向前绘制',branch_length)
        turtle.right(20)
        print('向右转角20')
        draw_branch(branch_length - 15)

    # 绘制左侧树枝
        turtle.left(40)
        print('向左转角40')
        draw_branch(branch_length - 15)

    # 向反方向绘制回到起始点
        if branch_length >= 15:
            turtle.pencolor('brown')
        turtle.right(20)
        print('向右转角20')
        turtle.backward(branch_length)
        print('向后绘制', branch_length)
def main():
    """"
    主函数
    """
    turtle.left(90)
    turtle.color('brown')
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    draw_branch(80)
    # 点击关闭
    turtle.exitonclick()

    """"
    直接调用主函数
    """

if  __name__  =='__main__':
    main()
