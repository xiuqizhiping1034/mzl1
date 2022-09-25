import turtle
def drawgap():##每段之间10间隔
    turtle.penup()
    turtle.forward(10)
def drawline(draw):##单段
    drawgap()
    turtle.pendown() if draw else turtle.penup()##draw为true则down,反之则up
    turtle.forward(50)
    drawgap()
    turtle.right(90)
def drawdigit(digit):##七段 根据参数digit决定要绘制的数字
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)
def drawdate(date):##获得要输出的日期
    turtle.pencolor("red")
    for i in date:
        turtle.pencolor("red")
        if i.isdigit():
            drawdigit(int(i))
        else:
            turtle.pencolor("green")
            turtle.write(i)
            turtle.forward(40)
def main():
    turtle.setup(1000,400,200,200)
    turtle.penup()
    turtle.forward(-400)
    turtle.pensize(5)
    date = input("Enter the date(xxxx年xx月xx日): ")
    drawdate(date)
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    main()