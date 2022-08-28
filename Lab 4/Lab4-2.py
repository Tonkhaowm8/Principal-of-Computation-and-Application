from matplotlib import pyplot
import math

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

    #def distance(self, other):
        #x_distance = 0
        #dis = math.sqrt(a**2+b**2)

    