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
        dis = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
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

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return "(%s, %s)" % (self.point1, self.point2) 

    def draw(self, t):
        if self.point1.get_x() > self.point2.get_x():
            t.penup()
            t.goto(self.point1.get_x(), self.point1.get_y())
            t.pendown()
            t.goto(self.point2.get_x(), self.point2.get_y())
            return(self.point2)
        else:
            t.penup()
            t.goto(self.point2.get_x(), self.point2.get_y())
            t.pendown()
            t.goto(self.point1.get_x(), self.point1.get_y())
            return(self.point1)

    #def join(self, line2):

#class 

def start():
    t = turtle.Turtle()
    turtle.screensize(canvwidth=500, canvheight=500)
    numPoint = random.randint(2, 10)
    pointArr = []
    for i in range(numPoint):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        t.penup()
        t.goto(x,y)
        t.dot()
        pointArr.append(Point(x, y))
    
    for i in range(len(pointArr)):
        try:
            line = Line(pointArr[i], pointArr[i + 1])
            line.draw(t)
        except:
            while 1:
                hello = 0

start()

        