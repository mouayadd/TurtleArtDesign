import turtle #brings in turtle
from mydesignfunctions import * #brings in all functions from other file
bob = turtle.Turtle() #gives turtle the name "bob"
turtle.bgcolor('black') # makes the background screen black
bob.speed(0) #fastest speed the turtle can draw at
turtle.colormode(255) # allows me to use rgb color system

for times in range(400): #performs a loop which creates a certain shape
    bob.color(204,204,0)#uses a type of yellow color
    bob.forward(times)
    bob.right(98)

for times in range(400): #performs another loop creating the same shape
    bob.color(0,255,255)#uses a different color then the previous shape
    bob.penup()
    bob.goto(0,0) #starts at home and overlaps the first shape
    bob.pendown()
    bob.forward(times)
    bob.right(98)


for times in range(400): #performs another loop creating the same shape
    bob.color(255,153,51) #uses a shade of orange
    bob.penup() #pulls the pen up to make sure no lines are drawn when moving
    bob.goto(0,0)
    bob.pendown()#drops the pen in order to start drawing again 
    bob.forward(times)
    bob.right(98)

draw_star(30,"orange") #calls in function draw_star from other file
                       #draws an orange star

