#64011164 Siraphop Mukdaphetcharat
import turtle
turtle.screensize(500, 500)
turtle.speed(10)

def draw(distance):
    if distance < 20:
        hello = 0 # Return function
    else:
        turtle.forward(distance) # Forward and turn left
        turtle.left(35)
        draw(3 * distance / 4) # recursion 1 for branches
        turtle.right(70)
        draw(3 * distance / 4) # recursion 2 for branches
        turtle.left(35)
        turtle.backward(distance) # back to original position

while True:
    draw(85)