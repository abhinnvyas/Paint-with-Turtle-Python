import turtle
import random

win = turtle.Screen()
tut = turtle.Turtle()
tut.speed(-1)
tut.shape('circle')
tut.width(10)

colors = ['red','green','blue','black','orange']

def dragging(x,y):
    tut.ondrag(None)
    tut.setheading(tut.towards(x,y))
    tut.goto(x,y)
    tut.ondrag(dragging)

def clickRight(x,y):
    tut.clear()

def up():
    tut.color(colors[random.randrange(0, len(colors))])

def main():
    turtle.listen()

    tut.ondrag(dragging)
    win.onscreenclick(clickRight,3)
    turtle.onkey(up,'w')

    win.mainloop()


main()
