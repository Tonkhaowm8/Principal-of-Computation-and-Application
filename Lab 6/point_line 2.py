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
    def __init__(self, pointLs):
        self.pointLs = pointLs

    def __str__(self):
        return self.pointLs

    def draw(self, t):
        

    

        