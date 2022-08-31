#64011614 Siraphop Mukdaphetcharat
import turtle

t = turtle.Turtle()
length = 100
angle = 20
first = True
t.screensize(canvwidth=500, canvheight=500)
t.penup()
t.goto(-450, 0)
def draw(branches, t, length, first):
    if branches != 0:
        if first:
            t.pendown()
            t.forward(length)
            length = length / 2
        else:
            t.pendown()
            t.right(angle)
            t.forward(length)
            t.backward(length)
            t.left(angle * 2)
        draw(branches-1, t, length, First)
