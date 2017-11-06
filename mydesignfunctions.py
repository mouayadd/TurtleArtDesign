import turtle   #brings in turtle
bob = turtle.Turtle() #gives turtle the name bob

def draw_star(size,color): #creates a function 
    bob.penup #pulls the pen up to make sure no lines are drawn when moving
    bob.goto(10,15)
    bob.pendown  #drops the pen in order to start drawing again
    angle=120
    bob.fillcolor(color)
    bob.begin_fill()

    for side in range(5): #loop used as a part of the function to draw a star
        bob.forward(size)
        bob.right(angle)
        bob.forward(size)
        bob.right(72-angle)
    bob.end_fill()
    return
