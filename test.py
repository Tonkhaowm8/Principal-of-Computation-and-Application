import turtle
import numpy as np

tlist = list()
colorlist = ["red", "green", "black", "blue", "brown"]
for i in range(5):
    tlist.append(turtle.Turtle(shape="turtle"))
    tlist[i].color(colorlist[i])
    tlist[i].speed(1)
screen = turtle.getscreen()
for i in range(100):
    screen.tracer(5)
    for t in tlist:
        t.right((np.random.rand(1) - .5) * 180)
        t.forward(int((np.random.rand(1) - .5) * 100))
    screen.update()