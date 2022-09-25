import turtle as t

def draw_Htree(x,y,l,n):
    if n==0 :
        return
    draw_H(x,y,l)
    draw_Htree(x-l/2,y+l/2,l/2,n-1)
    draw_Htree(x+l/2,y+l/2,l/2,n-1)
    draw_Htree(x - l / 2, y - l / 2, l / 2, n - 1)
    draw_Htree(x + l / 2, y - l / 2, l / 2, n - 1)

def draw_H(x,y,l):
    t.pencolor('red')
    draw_line(x-l/2,y,x+l/2,y)
    t.pencolor('green')
    draw_line(x-l/2,y+l/2,x-l/2,y-l/2)
    t.pencolor('blue')
    draw_line(x+l/2,y+l/2,x+l/2,y-l/2)

def draw_line(x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    t.penup()

def main():
    draw_Htree(0,0,100,5)
    t.done()

if __name__ == '__main__':
    main()