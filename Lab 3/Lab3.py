import turtle

#setting the clock
def generate_clock(): #generate clock
    radius = 150
    t.speed(0)
    t.penup()
    t.goto(0,(-radius))
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(0,0) #origin at (0,0)
    t.dot(10)
    angle = 0
    while angle != 360:
        t.setheading(angle)
        if angle % 30 == 0:
            t.forward(radius - 10)
            t.pendown()
            t.forward(20)
            t.penup()
            t.goto(0,0)
        else:
            t.forward(radius)
            t.pendown()
            t.dot(3)
            t.penup()
            t.goto(0,0)
        angle += 6

def clock_hand(hours, minutes, seconds):
    t.goto(0,0) #set turtle at origin
    # Seconds Hand
    seconds_angle = - seconds * 6 + 90
    print(seconds_angle)
    t.setheading(0)
    t.setheading(seconds_angle)
    t.pendown()
    t.forward(130)
    t.penup()
    # Minutes Hand
    minutes_hand = - minutes * 6 - seconds * 0.1 + 90
    print(minutes_hand)
    t.color("Green")
    t.goto(0,0)
    t.setheading(0)
    t.setheading(minutes_hand)
    t.pendown()
    t.forward(120)
    t.penup()
    #Hour hand
    hour_hand = - hours * 30 - minutes * 0.5 - seconds * 0.00833 + 90
    print(hour_hand)
    t.color("Red")
    t.goto(0,0)
    t.setheading(0)
    t.setheading(hour_hand)
    t.pendown()
    t.forward(90)
    t.penup()

def start():
    global t 
    try:
        hour = int(input("Enter Hour: "))
        if hour > 24 or hour < 0:
            print("Please enter correct hour!!")
            start()
        minutes = int(input("Enter Minutes: "))
        if minutes > 60 or hour < 0:
            print("Please enter correct minutes!!")
            start()
        seconds = int(input("Enter Seconds: "))
        if seconds > 60 or hour < 0:
            print("Please enter correct seconds!!")
            start()
        t = turtle.Turtle()
        if hour > 12:
            hour = hour - 12
        generate_clock()
        clock_hand(hour,minutes,seconds)
    except ValueError:
        print("Please enter a number!!!")
        start()
    

start()


while True:
    hello = 0
