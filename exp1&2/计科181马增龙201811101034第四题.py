"""
                作者计科181 马增龙
                学号 201811101034
                时间 2020.9.25
                功能
                        1)实现棋盘绘制
                        2)先写出绘制小方格的绘制函数
                        3)利用boolean变量控制是否填充颜色
                        4）进一步行程函数（起点横坐标，起点纵坐标，颜色，边的颜色，是否填充）
                        5）利用双层嵌套循环，进行绘制控制
"""
import turtle as  t

def draw(x,y,w,fillcolor = "black",pencolor = "black",fill="False"):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pensize(3)
    t.pencolor(pencolor)
    if fill:
        t.fillcolor(fillcolor)
        t.begin_fill()
    for i in range(0,4):
        t.forward(w)
        t.left(90)
    if fill:
        t.end_fill()

def main():
    t.speed("fastest")
    L =eval(input("please input the length of the chess:"))
    w = L//8  #一个格子的 宽度

    draw(-L//2,-L//2,L,pencolor = "red",fill=False)

    for j in range(-L//2,L//2-w,2*w):
        for i in range(-L//2,L//2-w,2*w):
            draw(i,j,w,pencolor="black",fillcolor="black",fill="ture")

    for j in range(-L// 2+w, L // 2 , 2 * w):
        for i in range(-L // 2+w, L // 2, 2 * w):
            draw(i, j, w, fillcolor="black")

    t.hideturtle()
    t.done

    # 允许用户自己点击关闭
    t.exitonclick()
if __name__ == '__main__':
    main()