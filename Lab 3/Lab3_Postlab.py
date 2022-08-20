from mimetypes import init
from re import T
import turtle
import random


class TurtleFRO():
    def __init__ (self, energy, color, position):
        self.t = turtle.Turtle()
        self.color = turtle.color(color)
        self.energy = energy

    def normal(self):
        self.pendown = turtle.pendown()
        self.move = turtle.forward(self.energy)
        self.penup = turtle.penup()

    def drunk(self):
        while self.energy != 0:
            self.rotate = turtle.setheading(random.randint(-360, 360))
            self.pendown = turtle.pendown()
            self.stamina = random.randint(-self.energy, self.energy)
            self.move = turtle.forward(self.stamina)
            self.energy = self.energy - abs(self.stamina)
        self.penup = turtle.penup()

normalTurtle = TurtleFRO(500, "Green")
normalTurtle.normal()
drunkTurtle = TurtleFRO(500, "Red")
drunkTurtle.drunk()

while True:
    hello = 0