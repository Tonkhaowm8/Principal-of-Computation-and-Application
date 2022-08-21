#Siraphop Mukdaphetcharat 64011614

from mimetypes import init
from re import T
import turtle
import random


class TurtleFRO():
    def __init__ (self, energy, color):
        self.t = turtle.Turtle(shape="turtle")
        self.t.color(color)

    def normal(self):
        self.t.pendown()
        self.t.forward(self.energy)
        self.t.penup()

    def drunk(self):
        self.t.setheading(random.randint(-360, 360))
        self.t.pendown()
        self.t.forward(random.randint(-50, 100))
        self.t.penup()
        self.t.speed(3)

    def on_crack(self):
        self.t.setheading(random.randint(-45, 45))
        self.t.pendown()
        self.t.forward(random.randint(0, 100))
        self.t.penup()
        self.t.speed(10)

    def autistic(self):
        self.t.setheading(random.randint(-30, 30))
        self.t.pendown()
        self.t.forward(random.randint(-50, 10))
        self.t.penup()
        self.t.speed(5)

turtle_list = list()

for i in range(5):
    turtle_list.append(TurtleFRO(10, "Green"))

for i in range(100):
    for j in range(len(turtle_list)):
        if j % 2 == 0:
            turtle_list[j].drunk()
        else:
            turtle_list[j].on_crack()