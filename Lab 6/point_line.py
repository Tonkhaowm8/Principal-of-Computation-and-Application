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

    def distance(self, a, b):
        dis = math.sqrt((a-self.x)**2+(b-self.y)**2)
        return dis

    def findClosest(self, point):
        closest = 10000
        for i in range(len(point)):
            for j in range (len(point)):
                x1 = point[j].get_x()
                x2 = point[i].get_x()
                y1 = point[j].get_y()
                y2 = point[i].get_y()
                deltaX, deltaY = abs(x1 - x2) ,abs(y1 - y2)
                totalCoords = deltaX + deltaY
                if totalCoords < closest and x1 != x2:
                    closest = totalCoords
                    outputCoords = [[x1, y1] , [x2, y2]]
                else:
                    continue
        return outputCoords

class Line(Point):
    def __init__(self, x_init, y_init):
        super().__init__(x_init, y_init)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def join(self, line2, t):
        line1 = []
        lineDistance = line2.distance(self.x, self.y)