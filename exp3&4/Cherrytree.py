import turtle
import random
from turtle import *
from time import sleep

def tree(branchlen,t):
    sleep(0.0005)
    if branchlen > 3:
        if 8 <= branchlen <= 12:
            if random.randint(0,2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')#淡珊瑚色
            t.pensize(branchlen/3)
        elif branchlen < 8:
            if random.randint(0,1) == 0:
                t.color('show')
            else:
                t.color('lightcoral')
            t.pensize(branchlen/2)
        else:
            t.color('sienna')#赭色
            t.pensize(branchlen/10)
        t.forward(branchlen)
        a = 1.5 * random.random()
        t.right(20*a)
        b = 1.5 * random.random()
        tree(branchlen-10*b,t)
        t.left(40*a)
        tree(branchlen-10*b,t)
        t.right(20*a)
        t.up()
        t.backward(branchlen)
        t.down()

def petal(m,t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')
        t.circle(1)
        t.up()
        t.forward(a)
        t.right(90)
        t.forward(b)

def main():
    t = turtle.Turtle()#绘图区域
    w = turtle.Screen()#画布大小
    t.hideturtle()
    getscreen().tracer(5,0)
    w.screensize(bg = 'wheat')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60,t)
    petal(200,t)
    w.exitonclick()

if __name__ == '__main__':
    main()