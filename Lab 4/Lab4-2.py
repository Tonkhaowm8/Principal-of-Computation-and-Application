from matplotlib import pyplot as plt
import math
import random

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
        self.coords = [[],[]]
    
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

    def findClosest(self):
        print(len(self.coords[0]))


def start():
    coords = []
    pointInput = int(input("Enter the number of Points: "))
    xArr, yArr = [], []
    for i in range(pointInput):
        xArr.append(random.randint(0, 1000))
        yArr.append(random.randint(0, 1000))
        p = Point(xArr[i], yArr[i])
        coords.append(p)
    while 1:
        plt.plot(xArr, yArr, 'ro')
        plt.show()

start()