#64011614 Siraphop Mukdaphetcharat
import turtle

t = turtle.Turtle()
length = 100
t.screensize(canvwidth=500, canvheight=500)
t.penup()
t.goto(-450, 0)
def draw(branches, t, length):
    if branches != 0:
        t.pendown()
        t.forward(length)
        length = length / 2
        draw(branches-1, t, length)
