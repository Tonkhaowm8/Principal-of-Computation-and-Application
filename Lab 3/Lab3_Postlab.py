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
        self.t.forward(100)
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

    def getPos(self):
        t = self.t.pos()
        return t[0]

    def stop(self):
        self.t.forward(0)

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

    inputArr = []
    for i in range(numTurtle):
        try:
            userSelection = int(input("(1) Normal Turtle (2) Drunk Turtle (3) On Crack Turtle (4) Autistic Turtle (5) Fat Turtle: "))
            if userSelection < 0 or userSelection > 5:
                print("Please enter the value between 1 - 5!!!")
            inputArr.append(userSelection)
        except ValueError:
            print("Please enter a number!!")
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

    finish = False
    for i in range(100): 
        for j in range(len(turtle_list)):
            if turtle_list[j].getPos() >= 400:
                finish = True
                break
            elif inputArr[j] == 1:
                turtle_list[j].normal()
            elif inputArr[j] == 2:
                turtle_list[j].drunk()
            elif inputArr[j] == 3:
                turtle_list[j].on_crack()
            elif inputArr[j] == 4:
                turtle_list[j].autistic()
            elif inputArr[j] == 5:
                turtle_list[j].fat()
            else:
                continue
                
        if finish:
            break
    if finish:
        for k in turtle_list:
            k.stop()

start()

