from mimetypes import init
from re import T
import turtle
import random


class TurtleFRO():
    def __init__ (self, energy, randomness, color):
        self.t = turtle.Turtle()
        self.color = turtle.color(color)
        

TurtleFRO(100, 10, "Green")