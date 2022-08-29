from matplotlib import pyplot as plt
import math
import random

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

    def distance(self, a, b, c, d):
        x_distance = 0
        dis = math.sqrt((a-c)**2+(b-d)**2)
        return d

    def findClosest(self, point):
        closest = 100
        firstCoords = []
        secondCoords = []
        for i in range(len(point)):
            for j in range (len(point)):
                deltaX, deltaY = abs(point[j].get_x - point[i].get_x) ,abs(point[j].get_y - point[i].get_y)
                totalCoords = deltaX + deltaY
                if totalCoords < closest:
                    closest = totalCoords
                    firstCoords, secondCoords = [point[j].get_x, point[j].get_y] , [point[i].get_x, point[i].get_y]
                else:
                    continue
        return firstCoords, secondCoords
        

def start():
    coords = []
    pointInput = int(input("Enter the number of Points: "))
    xArr, yArr = [], []
    for i in range(pointInput):
        xArr.append(random.randint(0, 1000))
        yArr.append(random.randint(0, 1000))
        p = Point(xArr[i], yArr[i])
        coords.append(p)
    closest = p.findClosest(coords)
    while 1:
        plt.plot(xArr, yArr, 'ro')
        plt.plot(closest[0], 'ro', color = 'blue')
        plt.plot(closest[1], 'ro', color = 'blue')
        plt.show()

start()