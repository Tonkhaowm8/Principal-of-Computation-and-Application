#64011614 Siraphop Mukdaphetcharat
import turtle

t = turtle.Turtle()

def draw(branches, t, length):
    if branches != 0:
        t.pendown()
        length = length ** branches
        t.forward(length)
        draw(branches-1, t)

def start():
    length = 5
    angle = 20
    first = True
    t.screensize(canvwidth=500, canvheight=500)
    t.penup()
    draw(10, t, length)
    t.goto(-450, 0)

while True:
    start()
    
