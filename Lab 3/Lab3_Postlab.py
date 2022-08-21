#Siraphop Mukdaphetcharat 64011614

#imports
import turtle
import random
import numpy as np

class TurtleFRO():
    def __init__ (self, energy, color): # Add turtle and colors
        self.t = turtle.Turtle(shape="turtle")
        self.t.color(color)

    def setPos(self, position): #set initial positions for each turtle
        self.t.penup()
        self.t.goto(-400 , position - 250)

    def normal(self, energy): # normal turtle function where it walks as a straight line
        usedEnergy = random.randint(0, 20)
        self.t.pendown()
        self.t.forward(usedEnergy) 
        self.t.penup()
        energy -= usedEnergy
        return energy

    def drunk(self, energy): # drunk turtle where the turtle will spins randomly
        usedEnergy = random.randint(-50, 100)
        self.t.speed(3)
        self.t.setheading(random.randint(-360, 360))
        self.t.pendown()
        self.t.forward(usedEnergy)
        self.t.penup()
        energy -= usedEnergy
        return energy

    def on_crack(self, energy): # where the turtle is super energetic
        usedEnergy = random.randint(0, 100)
        self.t.speed(10)
        self.t.setheading(random.randint(-45, 45))
        self.t.pendown()
        self.t.forward(usedEnergy)
        self.t.penup()
        energy -= usedEnergy
        return energy
        
    def autistic(self, energy): # Where the turtle mainly moves backwards
        usedEnergy = random.randint(-10, 20)
        self.t.speed(5)
        self.t.setheading(random.randint(-30, 30))
        self.t.pendown()
        self.t.forward(usedEnergy)
        self.t.penup()
        energy -= usedEnergy
        return energy

    def fat(self, energy): # Where the turtle moves the slowest
        usedEnergy = random.randint(0, 10)
        self.t.speed(10)
        self.t.pendown()
        self.t.forward(usedEnergy)
        self.t.penup()
        energy -= usedEnergy
        return energy

    def getPos(self): # Get position of the turtle and return it in x-axis integer value
        t = self.t.pos()
        return t[0]

    def stop(self): # Stop function to stop the turtle from moving
        self.t.forward(0)

turtle_list = list() # Creating a list of turtles

def line_creator(): # Creating a line for starting position and stopping position
    t = turtle.Turtle()
    t.speed(10)
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


def start(): # Start function

    colorArr = ["Red", "Blue", "Green", "Yellow", "Black", "Brown", "Pink", "Orange"] # Color array for selecting colors
   
    try:
        numTurtle = int(input("Enter number of turtles: ")) # User Input the abount of turtles to spawn
    except ValueError: # if user enters anything other than integer
        print("Please enter a number!!!")
        start()
    if numTurtle < 1 or numTurtle > 5: # if the number is less then 1 or more than 5
        print("The number of turtle cannot be less than 1 and exceed 5")
        start()

    inputArr = []
    for i in range(numTurtle): # asks user to select roles for the turtle they choose
        try:
            userSelection = int(input("(1) Normal Turtle (2) Drunk Turtle (3) On Crack Turtle (4) Autistic Turtle (5) Fat Turtle: "))
            if userSelection < 0 or userSelection > 5:
                print("Please enter the value between 1 - 5!!!")
                exit()
            enerArr = [userSelection, random.randint(400, 1000)]
            inputArr.append(enerArr)
        except ValueError: # if user enters anything other than an integer
            print("Please enter a number!!")
            start()

    turtle.screensize(canvwidth=500, canvheight=500) # Set the screen size for the turtle race
    line_creator()
    
    for i in range(numTurtle): # spawning and formatting the turtles
        randNum = random.randint(0,len(colorArr)-1)
        turtle_list.append(TurtleFRO(10, colorArr[randNum]))
        colorArr.pop(randNum)

    for i in range(len(turtle_list)): #evenly distribute turtles using numpy
        t = np.linspace(0, 500, numTurtle + 2)
        turtle_list[i].setPos(t[i+1])

    finish = False
    for i in range(100):  # Moving the turtle
        for j in range(len(turtle_list)):
            if turtle_list[j].getPos() >= 400: # When the turtle gets to the finis line
                finish = True
                break
            elif inputArr[j][0] == 1:
                if inputArr[j][1] <=0: # No energy left
                    turtle_list[j].stop()
                else:
                    inputArr[j][1] = turtle_list[j].normal(inputArr[j][1]) # Moving Normally
            elif inputArr[j][0] == 2:
                if inputArr[j][1] <=0:
                    turtle_list[j].stop()
                else:
                    inputArr[j][1] = turtle_list[j].drunk(inputArr[j][1])
            elif inputArr[j][0] == 3:
                if inputArr[j][1] <=0:
                    turtle_list[j].stop()
                else:
                    inputArr[j][1] = turtle_list[j].on_crack(inputArr[j][1])
            elif inputArr[j][0] == 4:
                if inputArr[j][1] <=0:
                    turtle_list[j].stop()
                else:
                    inputArr[j][1] = turtle_list[j].autistic(inputArr[j][1])
            elif inputArr[j][0] == 5:
                if inputArr[j][1] <=0:
                    turtle_list[j].stop()
                else:
                    inputArr[j][1] = turtle_list[j].fat(inputArr[j][1])
            else:
                continue
                
        if finish: # break when the turtle reaches the finish line
            break
    if finish:
        for k in turtle_list:
            k.stop()

start()

