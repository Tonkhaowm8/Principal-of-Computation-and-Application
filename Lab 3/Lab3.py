import turtle
#initiate turtle
t = turtle.Turtle()
#setting the clock
def generate_clock(): #generate clock
    radius = 150
    t.penup()
    t.goto(0,(-radius))
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(0,0) #origin at (0,0)
    angle = 0
    while angle != 360:
        t.setheading(angle)
        t.forward(1)
        t.pendown()
        t.forward(20)
        t.penup()
        t.goto(0,0)
        angle += 30

def clock_hand(hours, minutes, seconds):
    t.goto(0,0) #set turtle at origin
    seconds_angle = seconds * 6
    t.setheading(0)
    t.setheading(seconds_angle)
    t.pendown()
    t.forward(100)



generate_clock()
clock_hand(1,1,30)
