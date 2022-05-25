# Write a program to draw some kind of picture. 
# Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.

import turtle
import math

height = 1071
width = 700
screen = turtle.Screen()
screen.setup(width, height)

spurs = turtle.Turtle()
spurs.shape('square')
spurs.shapesize(.4)
spurs.pensize(8)
spurs.speed(5)

# lower football
spurs.penup()
spurs.goto(-50, -350)
spurs.pendown()
spurs.speed(5)
spurs.circle(100)
spurs.penup()
spurs.goto(-140, -207)
spurs.pendown()
spurs.speed(5)
spurs.circle(-25, 190)
spurs.penup()

# upper football seam
spurs.goto(-120, -213)
spurs.pendown()
spurs.speed(5)
spurs.left(35)
spurs.circle(250, -35)   

# middle football seam
spurs.penup()
spurs.goto(-115, -235)
spurs.pendown()
spurs.right(25)
spurs.circle(-375, -25)
spurs.penup()


# draw a semicircle
# turtle.circle(120, 180)  

screen = turtle.getscreen()

ts.getcanvas().postscript(file='spurs.eps')


#screen.exitonclick()










