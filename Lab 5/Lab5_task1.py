#64011614 Siraphop Mukdaphetcharat
import turtle

def draw(branches, length):
    t = turtle.Turtle()
    t.screensize(canvwidth=500, canvheight=500)
    t.penup()
    t.goto(-450, 0)
    if branches != 0:
        t.pendown()
        length = length ** branches
        t.forward(length)
        draw(branches-1, t)

def start():
    length = 5
    angle = 20
    first = True
    draw(10, length)
    

while True:
    draw(10, 5)
    
