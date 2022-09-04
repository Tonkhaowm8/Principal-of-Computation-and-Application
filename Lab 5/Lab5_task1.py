#64011614 Siraphop Mukdaphetcharat
import turtle
import numpy as np

t = turtle.Turtle()

def draw(branches):
    if branches >= 0:
        t.penup()
        xArr = np.linspace(-400,400, num=branches, endpoint=False)
        print(xArr)
        yArr = []
        for i in range(branches):
            y = np.linspace(-400, 400, num=(2**(i)), endpoint=False)
            yArr.append(y)
        for i in range(1,len(xArr)-1):
            for j in range(1,len(yArr[i])):
                t.goto(xArr[i], yArr[i][j])
                t.pendown()
                t.dot()
                t.penup()
        draw(branches - 1)
    else:
        return 0

def start():
    length = 5
    turtle.screensize(canvwidth=500, canvheight=500)
    draw(5)
    #t.goto(-450, 0)

while True:
    start()
    
