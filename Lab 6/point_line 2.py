#Siraphop Mukdaphetcharat 64011614
import random
import math
import turtle

# Class point from Lab 4
class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)


class Line():
    def __init__(self, pointLs, t):
        self.pointLs = pointLs
        self.turtle = t

    def __str__(self):
        return self.pointLs

    def draw(self):
        for i in self.pointLs:
            self.turtle.penup()
            x, y = i.get_x(), i.get_y()
            self.turtle.pendown()
            self.turtle.goto(x, y)
            self.turtle.penup()
    

        