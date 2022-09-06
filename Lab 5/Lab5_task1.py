#64011164 Siraphop Mukdaphetcharat
import turtle
turtle.screensize(500, 500)
turtle.speed(10)

def draw(distance):
    if distance < 20:
        hello = 0 # Return function
    else:
        angle = distance 
        turtle.forward(distance) # Forward and turn left
        turtle.left(30)
        draw(3 * distance / 4) # recursion 1 for branches
        turtle.right(60)
        draw(3 * distance / 4) # recursion 2 for branches
        turtle.left(30)
        turtle.backward(distance) # back to original position

while True:
    draw(85)