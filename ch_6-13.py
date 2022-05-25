# Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. 
# Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending 
# point of the last square when the program ends.)

'''import turtle

def drawsquare(t, sz):
	for i in range(4):
		t.forward(sz)
		t.left(90)

screen = turtle.Screen()
screen.bgcolor('grey')

randy = turtle.Turtle()
randy.color('pink')

for a in range(5):
	drawsquare(randy, 20)
	randy.penup()
	randy.forward(40)
	randy.pendown()

screen.exitonclick()'''

# Write a program to draw this. Assume the innermost square is 20 units per side, 
# and each successive square is 20 units bigger, per side, than the one inside it.

import turtle

def draw_big(t, sz):
	for i in range(4):
		t.forward(sz + 20)
		t.left(90)

screen = turtle.Screen()
screen.bgcolor('white')

rick = turtle.Turtle()
rick.color('purple')

draw_big(rick, 20)

screen.exitonclick()


# Write a non-fruitful function drawPoly(someturtle, somesides, somesize) 
# which makes a turtle draw a regular polygon. When called with drawPoly(tess, 8, 50), 
# it will draw a shape like this:



# Draw this pretty pattern.


# The two spirals in this picture differ only by the turn angle. Draw both.



# Write a non-fruitful function drawEquitriangle(someturtle, somesize) 
# which calls drawPoly from the previous question to have its turtle draw a equilateral triangle.



# Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. 
# So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.



# Write a function areaOfCircle(r) which returns the area of a circle of radius r. 
# Make sure you use the math module in your solution.


# Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.



# Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, 
# turn right by 144, put the pen down, and draw the next star. You’ll get something like this 
# (note that you will need to move to the left before drawing your first star in order to fit everything in the window):



# Extend the star function to draw an n pointed star. 
# (Hint: n must be an odd number greater or equal to 3).



# Write a function called drawSprite that will draw a sprite. 
# The function will need parameters for the turtle, the number of legs, and the length of the legs. 
# Invoke the function to create a sprite with 15 legs of length 120.



# Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n. 
# This time use the accumulator pattern.



# Write a function called mySqrt that will approximate the square root of a number, call it n, 
# by using Newton’s algorithm. Newton’s approach is an iterative guessing 
# algorithm where the initial guess is n/2 and each subsequent guess is computed using the 
# formula: newguess = (1/2) * (oldguess + (n/oldguess)).


# Write a function called myPi that will return an approximation of PI (3.14159…). 
# Use the Leibniz approximation.


# Write a function called myPi that will return an approximation of PI (3.14159…). Use the Madhava approximation.



# Write a function called fancySquare that will draw a square with fancy corners (sprites on the corners). 
# You should implement and use the drawSprite function from above. For an even more interesting look, 
# how about adding small triangles to the ends of the sprite legs.



# There was a whole program in A Turtle Bar Chart to create a bar chart with specific data. 
# Creating a bar chart is a useful idea in general. Write a non-fruitful function called barChart, 
# that takes the numeric list of data as a parameter, and draws the bar chart. 
# Write a full program calling this function. 
# The current version of the drawBar function unfortunately draws the top of the bar 
# through the bottom of the label. A nice elaboration is to make the label appear completely above the top line. 
# To keep the spacing consistent you might pass an extra parameter to drawBar for the distance to move up. 
# For the barChart function make that parameter be some small fraction of maxheight+border. 
# The fill action makes this modification particularly tricky: You will want to move past 
# the top of the bar and write before or after drawing and filling the bar.



