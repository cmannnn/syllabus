# CHAPTER 2 EXERCISES

# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), 
# and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on the clock when the alarm goes off.

'''while True:
	try:
		timez = int(input('Enter the time: '))
		if timez not in range(24):
			print('invalid time, please try again')
			continue
	except ValueError:
		print('invalid time, please try again')
		continue
	else:
		break
	
alarm = int(input('Enter how many hours until alarm: '))
alarm_time = timez + alarm
if alarm_time > 24:
	alarm_time = alarm_time // 24
	print('Alarm will ring at: {} o\'clock'.format(alarm_time))
if alarm_time == 24:
	print('Alarm will ring at: 00 o\'clock')'''

'''_____________________________________________________________________________________________'''

# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. 
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) 
# and you return home after 10 nights you would return home on a Saturday (day 6) 
# Write a general version of the program which asks for the starting day number, 
# and the length of your stay, and it will tell you the number of day of the week you will return on.

'''valid_entry = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

while True:
	try:
		start_date = input('What day of the week are you leaving? ')
		if start_date.lower() not in valid_entry:
			print('Enter a valid start date')
			continue
	except ValueError:
		print('Enter a valid start date')
		continue
	else:
		break

while True:
	try:
		vaca = int(input('How many day(s) is your stay? '))
	except vaca < 1:
		print('Enter a number greater than 1')
	except ValueError:
		print('Enter a valid number')
		continue 
	else:
		break

if start_date == 'sunday':
	day = 1
if start_date == 'monday':
	day = 2
if start_date == 'tuesday':
	day = 3
if start_date == 'wednesday':		
	day = 4
if start_date == 'thursday':
	day = 5
if start_date == 'friday':
	day = 6
if start_date == 'saturday':
	day = 7

back_date = day + vaca

# retrieve the start_date value + vaca and then convert back to date

if back_date > 7:
	back_date = back_date % 7
if back_date == 1:
	print('You will return on a Sunday')
if back_date == 2:
	print('You will return on a Monday')
if back_date == 3:
	print('You will return on a Tuesday')
if back_date == 4:
	print('You will return on a Wednesday')
if back_date == 5:
	print('You will return on a Thursday')
if back_date == 6:
	print('You will return on a Friday')
elif back_date == 7:
		print('You will return on a Saturday')'''

'''_____________________________________________________________________________________________'''

# Take the sentence: All work and no play makes Jack a dull boy. 
# Store each word in a separate variable, then print out the sentence on one line using print.

'''word_0 = ''
word_1 = ''
word_2 = ''
word_3 = ''
word_4 = ''
word_5 = ''
word_6 = ''
word_7 = ''
word_8 = ''
word_9 = ''

sent = 'All work and no play makes Jack a dull boy.'

word = sent.split()

word_0 = word_0 + word[0]
word_1 = word_1 + word[1]
word_2 = word_2 + word[2]
word_3 = word_3 + word[3]
word_4 = word_4 + word[4]
word_5 = word_5 + word[5]
word_6 = word_6 + word[6]
word_7 = word_7 + word[7]
word_8 = word_8 + word[8]
word_9 = word_9 + word[9]

print(word_0, word_1, word_2, word_3, word_4, word_5, word_6, word_7, word_8, word_9)'''

'''_____________________________________________________________________________________________'''

# Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

'''print(6 * 1 - 2)
print(6 * (1 - 2))'''

'''_____________________________________________________________________________________________'''

# The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
# (LOOK UP) formula for compound interest
# Write a Python program that assigns the principal amount of 10000 to variable P, 
# assign to n the value 12, and assign to r the interest rate of 8% (0.08). 
# Then have the program prompt the user for the number of years, t, that the money will be compounded for. 
# Calculate and print the final amount after t years.

'''def compound_ir(principal, rate, n_times, time):
	try:
		amount = principal * (1+(rate/n_times)) ** (n_times*time)
	except ValueError:
		print('Please enter a valid number')
	return round(amount, 3)

principal = float(input('What is the principal amount? '))
rate = float(input('What is the nominal interest rate (decimal) '))
if rate > 1.0:
		print('Please enter your interest rate as a decimal')
		quit()
n_times = float(input('How many times is the interest compounding /year? '))
time = float(input('How many years is the loan? '))

print(compound_ir(principal, rate, n_times, time))'''

'''_____________________________________________________________________________________________'''

# Write a program that will compute the area of a circle. 
# Prompt the user to enter the radius and print a nice message back to the user with the answer.

'''import math as m

def circle_area(radius):	
	while True:
		try:
			area = m.pi * (float(radius)**2)
			return area
		except ValueError:
			print('Enter a number')
			quit()
		else:
			quit()

radius = input('Enter the radius: ')

print('The area of your delightful circle is {}'.format(circle_area(radius)))'''

'''_____________________________________________________________________________________________'''

#Write a program that will compute the area of a rectangle. 
# Prompt the user to enter the width and height of the rectangle. 
# Print a nice message with the answer.

'''def tangle(length, height):
	while True:
		try:
			area = float(length) * float(height)
			return area
		except ValueError:
			print('Please enter a number')
			quit()
		else:
			quit()
	
length = input('Please enter a rectangle length: ')
height = input('Please enter a rectangle height: ')
if height == length:
	print('we calculating rectangles not squares!')
	
print('The area of your rectangle is: {}'.format(tangle(length, height)))'''

'''_____________________________________________________________________________________________'''

# Write a program that will compute MPG for a car. 
# Prompt the user to enter the number of miles driven and the number of gallons used. 
# Print a nice message with the answer.

'''def mpg(miles, gas):
	while True:
		try:
			calc = float(miles) / float(gas)
			return calc
		except ValueError:
			print('Please enter a number')
			quit()
		else:
			quit()

miles = input('Enter the number of miles driven: ')
gas = input('Enter the number of gallons used: ')

print('Your MPG for the trip is: {}'.format(mpg(miles, gas)))'''

'''_____________________________________________________________________________________________'''

#Write a program that will convert degrees Celsius to degrees Fahrenheit.

'''def c_f(temp_c):
	while True:
		try:
			temp_f = float(temp_c) * 1.8 + 32
			return round(temp_f, 2)
		except ValueError:
			print('Please enter a valid temp')
			quit()
		else:
			quit()

temp_c = input('Enter a temp in Celsius: ')

print('The temp is {} degrees Fahrenheit'.format(c_f(temp_c)))'''

'''_____________________________________________________________________________________________'''

# Write a program that will convert degrees Fahrenheit to degrees Celsius.

'''def f_c(tempy_f):
	while True:
		try:
			tempy_c = (float(tempy_f) - 32) / 1.8
			return round(tempy_c, 1)
		except ValueError:
			print('Please enter a valid temp')
			quit()
		else:
			quit()

tempy_f = input('Enter a temp in Fahrenheit: ')

print('The temp is {} degrees Celsius'.format(f_c(tempy_f)))'''

'''_____________________________________________________________________________________________'''

'''import turtle

wm = turtle.Screen()
wm.bgcolor('lightgreen')

alex = turtle.Turtle()
alex.color('blue')
alex.pensize(4)

alex.forward(150)
alex.left(90)
alex.forward(100)
alex.forward(75)

wm.exitonclick()'''

'''_____________________________________________________________________________________________'''

#Extend this program …

# Modify this program so that before it creates the window, 
# it prompts the user to enter the desired background color. 
# It should store the user’s responses in a variable, and modify the 
# color of the window according to the user’s wishes. 
# (Hint: you can find a list of permitted color names at 
# https://www.w3schools.com/colors/colors_names.asp. 
# It includes some quite unusual ones, like “PeachPuff” and “HotPink”.)

# Do similar changes to allow the user, at runtime, to set tess’ color.

# Do the same for the width of tess’ pen. Hint: your dialog with the user will return a string, 
# but tess’ pensize method expects its argument to be an int. That means you need to convert the 
# string to an int before you pass it to pensize.

'''import turtle
import random

colors = [
	'AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure',' Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue',	'BlueViolet',
	'Brown',	'BurlyWood',	'CadetBlue',	'Chartreuse',	'Chocolate',	'Coral',	'CornflowerBlue',
	'Cornsilk',	'Crimson',	'Cyan',	'DarkCyan',	'DarkGoldenRod',	'DarkGray',	'DarkGrey',	'DarkGreen',	'DarkKhaki',	'DarkMagenta',	
	'DarkOliveGreen',	'DarkOrange',	'DarkOrchid',	'DarkRed',
	'DarkSalmon',	'DarkSeaGreen',	'DarkSlateBlue',	'DarkSlateGray',	'DarkSlateGrey',	'DarkTurquoise',	'DarkViolet',
	'DeepPink',	'DeepSkyBlue',	'DimGray',	'DimGrey',	'DodgerBlue',	'FireBrick',	'FloralWhite',	'ForestGreen',	'Fuchsia',
	'Gainsboro',	'GhostWhite',	'Gold',	'GoldenRod',	'Gray',	'Grey',	'Green',	'GreenYellow',	'HoneyDew',
	'HotPink',	'IndianRed',	'Indigo',	'Ivory',	'Khaki',	'Lavender',	'LavenderBlush',	'LawnGreen',	'LemonChiffon',	'LightBlue',
	'LightCoral',	'LightCyan',	'LightGoldenRodYellow',	'LightGray',	'LightGrey',	'LightGreen',	'LightPink',	'LightSalmon',
	'LightSeaGreen',	'LightSkyBlue',	'LightSlateGray',	'LightSlateGrey','LightSteelBlue',	'LightYellow',	'Lime',
	'LimeGreen',	'Linen',	'Magenta',	'Maroon',	'MediumAquaMarine',	'MediumBlue',	'MediumOrchid',
	'MediumPurple',	'MediumSeaGreen',	'MediumSlateBlue',	'MediumSpringGreen',	'MediumTurquoise',	'MediumVioletRed',
	'MidnightBlue',	'MintCream',	'MistyRose',	'Moccasin',	'NavajoWhite',	'Navy',	'OldLace',	'Olive',	'OliveDrab',
	'Orange',	'OrangeRed',	'Orchid',	'PaleGoldenRod',	'PaleGreen',	'PaleTurquoise',	'PaleVioletRed',
	'PapayaWhip',	'PeachPuff',	'Peru',	'Pink',	'Plum',	'PowderBlue',	'Purple',	'Red',
	'RosyBrown',	'RoyalBlue',	'SaddleBrown',	'Salmon',	'SandyBrown',	'SeaGreen',	'SeaShell',	'Sienna',	'Silver',
	'SkyBlue',	'SlateBlue',	'SlateGray',	'SlateGrey',	'Snow',	'SpringGreen',	'SteelBlue','Tan',	'Teal',	'Thistle',
	'Tomato',	'Turquoise',	'Violet',	'Wheat',	'White',	'WhiteSmoke',	'Yellow',	'YellowGreen'
    ]

# background color input
bg_inny = input('What color would you like the background to be? (type a color, random, or help for a list of colors): ')

# turtle background input
sam_inny = input('What color would you like Sam to be? (type a color, random, or help for a list of colors): ')

size_inny = input('How big would you like Sam to be? (massive, large, medium, small): ')

# initialize screen
screen = turtle.Screen()

# set background color from user input or list
if bg_inny in colors:
	screen.bgcolor(bg_inny)
if bg_inny == 'random':
	screen.bgcolor(random.choice(colors))
if bg_inny.lower() == 'help':
	print(colors)
	quit()

# initiate turtle
sam = turtle.Turtle()
sam.shape('turtle')

# setting turtle size
if size_inny.lower() == 'massive':
	sam.shapesize(12,12,12)
if size_inny.lower() == 'large':
	sam.shapesize(8,8,8)
if size_inny.lower() == 'medium':
	sam.shapesize(4,4,4)
if size_inny.lower() == 'small':
	sam.shapesize(1,1,1) 

# set turtle color
if sam_inny in colors:
	sam.color(sam_inny)
if sam_inny == 'random':
	sam.color(random.choice(colors))
if sam_inny == 'help':
	print(colors)
	quit()

# draw a cool shape
for i in range(1):
	n = 10
	while n <= 100:
		sam.circle(n)
		n = n + 10
		sam.rt(45)

# exit on click
screen.exitonclick()'''

'''_____________________________________________________________________________________________'''

# Write a program that prints We like Python's turtles! 100 times.
'''for i in range(101):
	print('We like Python\'s turtles!')
print(i)'''

'''_____________________________________________________________________________________________'''

# Write a program that uses a for loop to print
	# One of the months of the year is January
	# One of the months of the year is February
	# One of the months of the year is March

'''for months in ['Janurary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
	print('One of the months of the year is', months)'''

'''_____________________________________________________________________________________________'''


# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
	# Write a loop that prints each of the numbers on a new line.
	# Write a loop that prints each number and its square on a new line.

'''for num in ['12', '10', '32', '3', '66', '17', '42', '99', '20']:
	print(num)
	print(int(num) ** 2)'''

'''_____________________________________________________________________________________________'''

# Use for loops to make a turtle draw these regular polygons 
# (regular means all sides the same lengths, all angles the same):
	# An equilateral triangle
'''import turtle

screen = turtle.Screen()
brad = turtle.Turtle()
brad.shape('turtle')

for i in range(1):
	brad.forward(100)
	brad.left(135)
	brad.forward(75)
	brad.left(90)
	brad.forward(75)

screen.exitonclick()'''

	# A square

'''import turtle

screen = turtle.Screen()
brad = turtle.Turtle()
brad.shape('turtle')

for i in range(4):
	brad.forward(100)
	brad.right(90)

screen.exitonclick()'''

	# A hexagon (six sides)

'''import turtle

screen = turtle.Screen()
jim = turtle.Turtle()
jim.shape('turtle')

for i in range(6):
	jim.forward(50)
	jim.right(60)

screen.exitonclick()'''

	# An octagon (eight sides)
'''import turtle
screen = turtle.Screen()
sarah = turtle.Turtle()
sarah.shape('turtle')

for i in range(8):
	sarah.forward(50)
	sarah.right(45)

screen.exitonclick()'''

'''_____________________________________________________________________________________________'''

# Write a program that asks the user for the number of sides, the length of the side, the color, 
# and the fill color of a regular polygon. The program should draw the polygon and then fill it in.

'''import turtle

# all available colors
colors = [
	'AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure',' Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue',	'BlueViolet',
	'Brown',	'BurlyWood',	'CadetBlue',	'Chartreuse',	'Chocolate',	'Coral',	'CornflowerBlue',
	'Cornsilk',	'Crimson',	'Cyan',	'DarkCyan',	'DarkGoldenRod',	'DarkGray',	'DarkGrey',	'DarkGreen',	'DarkKhaki',	'DarkMagenta',	
	'DarkOliveGreen',	'DarkOrange',	'DarkOrchid',	'DarkRed',
	'DarkSalmon',	'DarkSeaGreen',	'DarkSlateBlue',	'DarkSlateGray',	'DarkSlateGrey',	'DarkTurquoise',	'DarkViolet',
	'DeepPink',	'DeepSkyBlue',	'DimGray',	'DimGrey',	'DodgerBlue',	'FireBrick',	'FloralWhite',	'ForestGreen',	'Fuchsia',
	'Gainsboro',	'GhostWhite',	'Gold',	'GoldenRod',	'Gray',	'Grey',	'Green',	'GreenYellow',	'HoneyDew',
	'HotPink',	'IndianRed',	'Indigo',	'Ivory',	'Khaki',	'Lavender',	'LavenderBlush',	'LawnGreen',	'LemonChiffon',	'LightBlue',
	'LightCoral',	'LightCyan',	'LightGoldenRodYellow',	'LightGray',	'LightGrey',	'LightGreen',	'LightPink',	'LightSalmon',
	'LightSeaGreen',	'LightSkyBlue',	'LightSlateGray',	'LightSlateGrey','LightSteelBlue',	'LightYellow',	'Lime',
	'LimeGreen',	'Linen',	'Magenta',	'Maroon',	'MediumAquaMarine',	'MediumBlue',	'MediumOrchid',
	'MediumPurple',	'MediumSeaGreen',	'MediumSlateBlue',	'MediumSpringGreen',	'MediumTurquoise',	'MediumVioletRed',
	'MidnightBlue',	'MintCream',	'MistyRose',	'Moccasin',	'NavajoWhite',	'Navy',	'OldLace',	'Olive',	'OliveDrab',
	'Orange',	'OrangeRed',	'Orchid',	'PaleGoldenRod',	'PaleGreen',	'PaleTurquoise',	'PaleVioletRed',
	'PapayaWhip',	'PeachPuff',	'Peru',	'Pink',	'Plum',	'PowderBlue',	'Purple',	'Red',
	'RosyBrown',	'RoyalBlue',	'SaddleBrown',	'Salmon',	'SandyBrown',	'SeaGreen',	'SeaShell',	'Sienna',	'Silver',
	'SkyBlue',	'SlateBlue',	'SlateGray',	'SlateGrey',	'Snow',	'SpringGreen',	'SteelBlue','Tan',	'Teal',	'Thistle',
	'Tomato',	'Turquoise',	'Violet',	'Wheat',	'White',	'WhiteSmoke',	'Yellow',	'YellowGreen'
    ]

# number of sides input
sides = int(input('How many sides would you like the shape to have? '))
if int(sides) < 3:
	print('Please enter a number of sides greater than 2')
	quit()

# line color input
line_color = input('What color would you like the line to be? ')
if line_color not in colors:
	raise ValueError('Invalid color')
	quit()

# fill color input
fill_color = input('What color would you like the fill to be? ')
if fill_color not in colors:
	raise ValueError('Invalid color')
	quit()

# init screen
screen = turtle.Screen()

# init turtle
harry = turtle.Turtle()

# init turtle shape
harry.shape('turtle')
harry.shapesize(.3)

# init turtle pen size
harry.pensize(10)

# line color loop
line_color = harry.pen(pencolor=line_color)
fill_color = harry.pen(fillcolor=fill_color)

# just begin fill
harry.begin_fill()

# interior angle calculation
int_angle = (360 / sides)

# resizing size of shape based on # of sides 
for i in range(sides):
	if sides < 14:
		harry.forward(75)
		harry.left(int_angle)
# larger than 14 sides need to resize forward call
	if sides < 22 and sides > 14:
		harry.forward(50)
		harry.left(int_angle)
else:
	harry.circle(150)

# end fill call
harry.end_fill()

# exit screen on click
screen.exitonclick()'''

'''_____________________________________________________________________________________________'''

# A drunk pirate makes a random turn and then takes 100 steps forward, 
# makes another random turn, takes another 100 steps, turns another random amount, etc. 

# A social science student records the angle of each turn before the next 100 steps are taken. 
# Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) 
#Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading.

'''import turtle

# import screen
screen = turtle.Screen()

# create pirate
pirate = turtle.Turtle()

# pirate shape and size
pirate.shape('turtle')
pirate.shapesize(1)

# pirate pensize and color
pirate.pensize(8)
pirate.pen(pencolor='FireBrick')

# drunk pirate
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
	pirate.forward(100)
	pirate.left(angle)

print('The pirate turned: ', pirate.heading())

# exit on click
screen.exitonclick()'''

'''_____________________________________________________________________________________________'''

# Write a program to draw a shape like this: (star)

'''import turtle

screen = turtle.Screen()
jeff = turtle.Turtle()
jeff.shape('turtle')
jeff.shapesize(1)

jeff.pensize(8)
jeff.pen(pencolor='BurlyWood')
jeff.pen(fillcolor='PowderBlue')

jeff.penup()
jeff.left(90)
jeff.forward(100)
jeff.pendown()
jeff.begin_fill()
jeff.left(162)

for i in range(5):
	jeff.forward(200)
	jeff.left(144)
	
jeff.end_fill()
screen.exitonclick()'''

'''_____________________________________________________________________________________________'''

# Write a program to draw a face of a clock that looks something like this: (see picture)

'''import turtle

screen = turtle.Screen()
screen.bgcolor('MediumOrchid')
cat = turtle.Turtle()

cat.shape('turtle')
cat.shapesize(1)

cat.pensize(1)
cat.pen(pencolor='Chartreuse')

cat2 = cat.clone()
cat3 = cat.clone()
cat4 = cat.clone()
cat5 = cat.clone()
cat6 = cat.clone()
cat7 = cat.clone()
cat8 = cat.clone()
cat9 = cat.clone()
cat10 = cat.clone()
cat11 = cat.clone()
cat12 = cat.clone()
cat13 = cat.clone()

def all_cats(cat):
	cat.penup()
	cat.forward(90)
	cat.pendown()
	cat.forward(10)
	cat.penup()
	cat.forward(20)

all_cats(cat)
cat2.left(30)
all_cats(cat2)
cat3.left(60)
all_cats(cat3)
cat4.left(90)
all_cats(cat4)
cat5.left(120)
all_cats(cat5)
cat6.left(150)
all_cats(cat6)
cat7.left(180)
all_cats(cat7)
cat8.left(210)
all_cats(cat8)
cat9.left(240)
all_cats(cat9)
cat10.left(270)
all_cats(cat10)
cat11.left(300)
all_cats(cat11)
cat12.left(330)
all_cats(cat12)

screen.exitonclick()'''

'''_____________________________________________________________________________________________'''

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

screen.exitonclick()




'''_____________________________________________________________________________________________'''

# Create a turtle and assign it to a variable. When you print its type, what do you get?

'''_____________________________________________________________________________________________'''

# A sprite is a simple spider shaped thing with n legs coming out from a center point. 
# The angle between each leg is 360 / n degrees.
# Write a program to draw a sprite where the number of legs is provided by the user.







