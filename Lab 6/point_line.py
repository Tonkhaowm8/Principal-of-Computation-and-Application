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
    def __init__(self, point1, point2, t):
        self.point1 = point1
        self.point2 = point2
        self.t = t

    def get_point(self):
        return(self.point1, self.point2)

    def __str__(self):
        return "(%s, %s)" % (self.point1, self.point2) 

    def draw(self):
            self.t.penup()
            self.t.goto(self.point1.get_x(), self.point1.get_y())
            self.t.pendown()
            self.t.goto(self.point2.get_x(), self.point2.get_y())
            self.t.penup()

    def join(self, line2):
        points = line2.get_point()
        self.t.penup()
        self.t.goto(points[0].get_x(), points[0].get_y())
        self.t.pendown()
        self.t.goto(self.point2.get_x(), self.point2.get_y())
#hello

class LineTester():
    def __init__(self, t):
        self.t = t
    
    def test_join(self, points):
        pointArr = []
        lineArr = []
        # generating points
        for i in range(points):
            x = random.randint(-400, 400)
            y = random.randint(-400, 400)
            self.t.penup()
            self.t.goto(x,y)
            self.t.dot()
            self.t.write(f"P{i + 1}")
            pointArr.append(Point(x, y))

        for i in range(len(pointArr)):
            if i % 2 == 0:
                l = Line(pointArr[i], pointArr[i + 1], self.t)
                l.draw()
                lineArr.append(l)
        
        for i in range(len(lineArr)):
            try:
                joinLine = lineArr[i].join(lineArr[i + 1])
            except:
                continue
        

def start():
    t = turtle.Turtle()
    turtle.screensize(canvwidth=500, canvheight=500)
    tester = LineTester(t)
    tester.test_join(10)

start()

        