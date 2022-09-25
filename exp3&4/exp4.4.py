import turtle as t

def side(size,n):
    if n==0 :
        t.forward(size)
        return
    side(size/3,n-1)
    t.left(60)
    side(size / 3, n - 1)
    t.right(120)
    side(size / 3, n - 1)
    t.left(60)
    side(size / 3, n - 1)
def main():
    for i in range(0,5):
        side(300,3)
        t.right(120)
    t.done()
if __name__ == '__main__':
    main()