# Siraphop Mukdaphetcharat 64011614
from matplotlib import pyplot as plt
import math
import random
import timeit

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
    
    def get_x(self): # Return X coords
        return self.x
    
    def get_y(self): # Return Y coords
        return self.y

    def __repr__(self): # Join string
        return "".join(["(", str(self.x), ",", str(self.y), ")"])
    
    def __str__(self): # Return String
        return "(%s, %s)" % (self.x, self.y)

    def distance(self, a, b, c, d): # Return distance between 2 points
        dis = math.sqrt((a-c)**2+(b-d)**2)
        return dis

    def findClosest(self, point): # Return the coordinates of the closest 2 points, point is type list
        closest = 10000
        for i in range(len(point)):
            for j in range (len(point)): 
                x1 = point[j].get_x() # Get coordinates of both points
                x2 = point[i].get_x()
                y1 = point[j].get_y()
                y2 = point[i].get_y()
                deltaX, deltaY = abs(x1 - x2) ,abs(y1 - y2) # Find the difference between both points
                totalCoords = deltaX + deltaY # add the difference
                if totalCoords < closest and x1 != x2: # Check if the difference is less than stored value
                    closest = totalCoords
                    outputCoords = [[x1, y1] , [x2, y2]]
                else:
                    continue
        return outputCoords # Output as nested list
        

def start(pt):
    coords = []
    pointInput = pt
    xArr, yArr = [], []
    for i in range(pointInput): # random points
        xArr.append(random.randint(0, 1000))
        yArr.append(random.randint(0, 1000))
        p = Point(xArr[i], yArr[i])
        coords.append(p) # Store random points coordinates into a list
    # Timer
    startTime = timeit.default_timer()
    closest = p.findClosest(coords)
    endTime = timeit.default_timer()
    deltaT = endTime - startTime
    print(f"runtime is {round(deltaT, 3)}")
    # Plot the graph
    plt.plot(xArr, yArr, 'ro') 
    plt.plot([closest[0][0],closest[1][0]], [closest[0][1],closest[1][1]], color = 'blue')
    plt.plot(closest[0][0],closest[0][1], 'ro', color = 'blue')
    plt.plot(closest[1][0],closest[1][1], 'ro', color = 'blue')
    plt.show()
    return deltaT

#plotting big O graph
t = []
n = []
for i in range(10,1000,100):
    t.append(start(i))
    n.append(i)
while 1:
    plt.plot(n,t)
    plt.xlabel("n")
    plt.ylabel("time (Seconds)")
    plt.show()
