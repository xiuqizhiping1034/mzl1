"""
                作者 马增龙
                时间 2020.9.15
                功能
                        1)绘画出五角星
                        2)实现五角星的重叠绘制
                        3）利用迭代绘制五角星
                        4）利用函数绘画出八卦图
                        5）绘画出对称天元图
"""
import turtle
def draw_recursive_pentagram(size):
    """
        迭代绘制五角星
    """
    # 计数器
    count = 1;
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    # 五角星绘制完成
    size += 10
    # 实现参数的更新
    if size <= 150:
        draw_recursive_pentagram(size)
    #自我调用

def draw_Eight_Diagrams():
    """"
            绘画八卦图
    """
    turtle.penup()
    turtle.goto(100,150)
    turtle.pendown()
    # 隐藏光标
    turtle.hideturtle()

    window = turtle.Screen()

    bage = turtle.Turtle()

    radius = 100
    bage.width(3)
    bage.color("black", "black")
    bage.begin_fill()
    bage.circle(radius / 2, 180)
    bage.circle(radius, 180)
    bage.left(180)
    bage.circle(-radius / 2, 180)
    bage.end_fill()

    bage.left(90)
    bage.up()
    bage.forward(radius * 0.35)
    bage.right(90)
    bage.down()
    bage.color("white", "white")
    bage.begin_fill()
    bage.circle(radius * 0.15)
    bage.end_fill()

    bage.left(90)
    bage.up()
    bage.backward(radius * 0.7)
    bage.down()
    bage.left(90)
    bage.color("black", "black")
    bage.begin_fill()
    bage.circle(radius * 0.15)
    bage.end_fill()

    bage.right(90)
    bage.up()
    bage.backward(radius * 0.65)
    bage.right(90)
    bage.down()
    bage.circle(radius, 180)
    bage.ht()

def main():
    """"
    主函数
    """
    # 绘制多个重叠五角星

    # 对绘画笔进行一些调整 颜色 粗度 初始位置
    turtle.penup()
    turtle.goto(-140,280)
    turtle.write("计科181 马增龙 201811101034 ", move=True,align = "left", font = ("Arial",15,"normal"))
    turtle.goto(-330,-210)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    # # 初始长度
    size = 100
    """"
    调用递归五角星函数
    """
    draw_recursive_pentagram(size)
    # 移动光标位置
    turtle.up()
    turtle.goto(-330, 210)
    turtle.down()
    draw_recursive_pentagram(size)

    # 移动光标位置
    turtle.up()
    turtle.goto(210, 210)
    turtle.down()
    """"
    调用八卦图函数
    """
    draw_recursive_pentagram(size)


    turtle.up()
    turtle.goto(210, -210)
    turtle.down()
    draw_recursive_pentagram(size)

    # 移动光标位置
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()

    draw_Eight_Diagrams()
    # 允许用户自己点击关闭
    turtle.exitonclick()


    """"
    直接调用主函数
    """
if  __name__  =='__main__':
    main()
