from matplotlib import pyplot as plt
import math
import random
import timeit

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
        closest = 10000
        firstCoords = []
        secondCoords = []
        totalDict = {}
        smallest = 0
        for i in range(len(point)):
            for j in range (len(point)):
                x1 = point[j].get_x()
                x2 = point[i].get_x()
                y1 = point[j].get_y()
                y2 = point[i].get_y()
                deltaX, deltaY = abs(x1 - x2) ,abs(y1 - y2)
                totalCoords = deltaX + deltaY
                totalDict[totalCoords] = [[x1, y1], [x2, y2]]
        for i in range(100000):
            try:
                smallest = totalDict[i]
                if smallest[0][0] == smallest[1][0]:
                    continue
                else:
                    break
            except:
                continue
        return smallest
        

def start():
    coords = []
    pointInput = int(input("Enter the number of Points: "))
    xArr, yArr = [], []
    for i in range(pointInput):
        xArr.append(random.randint(0, 1000))
        yArr.append(random.randint(0, 1000))
        p = Point(xArr[i], yArr[i])
        coords.append(p)
    startTime = timeit.default_timer()
    closest = p.findClosest(coords)
    endTime = timeit.default_timer()
    print(f"runtime is {round(endTime - startTime, 3)}")
    while 1:
        plt.plot(xArr, yArr, 'ro')
        plt.plot([closest[0][0],closest[1][0]], [closest[0][1],closest[1][1]], color = 'blue')
        plt.plot(closest[0][0],closest[0][1], 'ro', color = 'blue')
        plt.plot(closest[1][0],closest[1][1], 'ro', color = 'blue')
        plt.show()

start()