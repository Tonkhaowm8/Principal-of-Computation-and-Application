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

    def setPos(self, position):
        self.t.penup()
        self.t.goto(-400 , position - 250)

    def normal(self):
        self.t.pendown()
        self.t.forward(self.energy)
        self.t.penup()

    def drunk(self):
        self.t.speed(3)
        self.t.setheading(random.randint(-360, 360))
        self.t.pendown()
        self.t.forward(random.randint(-50, 100))
        self.t.penup()

    def on_crack(self):
        self.t.speed(10)
        self.t.setheading(random.randint(-45, 45))
        self.t.pendown()
        self.t.forward(random.randint(0, 100))
        self.t.penup()
        
    def autistic(self):
        self.t.speed(5)
        self.t.setheading(random.randint(-30, 30))
        self.t.pendown()
        self.t.forward(random.randint(-10, 20))
        self.t.penup()

    def fat(self):
        self.t.speed(5)
        self.t.pendown()
        self.t.forward(random.randint(0, 20))
        self.t.penup()

turtle_list = list()

def line_creator():
    t = turtle.Turtle()
    t.penup()
    t.goto(-400, -500)
    t.setheading(90)
    t.pendown()
    t.forward(1000)
    t.penup()
    t.goto(400, -500)
    t.setheading(90)
    t.pendown()
    t.forward(1000)
    t.penup()

def start():

    colorArr = ["Red", "Blue", "Green", "Yellow", "Black", "Brown", "Pink", "Orange"]

   
    try:
        numTurtle = int(input("Enter number of turtles: "))
    except ValueError:
        print("Please enter a number!!!")
        start()
    if numTurtle < 1 or numTurtle > 5:
        print("The number of turtle cannot be less than 1 and exceed 5")
        start()

    turtle.screensize(canvwidth=500, canvheight=500)
    line_creator()
    
    for i in range(numTurtle):
        randNum = random.randint(0,len(colorArr)-1)
        turtle_list.append(TurtleFRO(10, colorArr[randNum]))
        colorArr.pop(randNum)

    for i in range(len(turtle_list)): #evenly distribute turtles using numpy
        t = np.linspace(0, 500, numTurtle + 2)
        turtle_list[i].setPos(t[i+1])

    typeTurtle = ["normal", "drunk", "on_crack", "autistic", "fat"]
    a = random.randint(0,len(typeTurtle)-1)
    for i in range(100): #
        for j in range(len(turtle_list)):
            turtle_list[j].fat()



start()

