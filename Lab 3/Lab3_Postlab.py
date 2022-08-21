#Siraphop Mukdaphetcharat 64011614

from mimetypes import init
from re import T
import turtle
import random
import numpy as np

class TurtleFRO():
    def __init__ (self, energy, color):
        self.t = turtle.Turtle(shape="turtle")
        self.t.color(color)

    def normal(self):
        self.t.pendown()
        self.t.forward(self.energy)
        self.t.penup()

    def drunk(self):
        self.t.setheading(random.randint(-360, 360))
        self.t.pendown()
        self.t.forward(random.randint(-50, 100))
        self.t.penup()
        self.t.speed(3)

    def on_crack(self):
        self.t.setheading(random.randint(-45, 45))
        self.t.pendown()
        self.t.forward(random.randint(0, 100))
        self.t.penup()
        self.t.speed(10)

    def autistic(self):
        self.t.setheading(random.randint(-30, 30))
        self.t.pendown()
        self.t.forward(random.randint(-10, 20))
        self.t.penup()
        self.t.speed(5)

turtle_list = list()

def start():
    turtle.screensize(canvwidth=500, canvheight=500)
    try:
        numTurtle = int(input("Enter number of turtles: "))
    except ValueError:
        print("Please enter a number!!!")
        start()
    if numTurtle < 1 or numTurtle > 5:
        print("The number of turtle cannot be less than 1 and exceed 5")
        start()
    return numTurtle

start()
colorArr = ["Red", "Blue", "Green", "Yellow", "Black", "Brown", "Pink", "Orange"]
for i in range(5):
    randNum = random.randint(0,len(colorArr)-1)
    turtle_list.append(TurtleFRO(10, colorArr[randNum]))
    colorArr.pop(randNum)

for i in range(100):
    for j in range(len(turtle_list)):
        turtle_list[j].autistic()