from mimetypes import init
from re import T
import turtle
import random


class TurtleFRO():
    def __init__ (self, energy, color):
        self.t = turtle.Turtle()
        self.color = turtle.color(color)
        while energy >= 0:
            self.rotate = turtle.setheading(random.randint(-360, 360))
            self.pendown = turtle.pendown()
            self.stamina = random.randint(-energy, energy)
            self.move = turtle.forward(self.stamina)
            energy = energy - abs(self.stamina)
            print(energy)
        

TurtleFRO(100, "Green")
while True:
    hello = 0