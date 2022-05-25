# Use a for statement to print 10 random numbers.
'''import random

for s in range(10):
	print(random.random())'''

# Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.
'''import random

for s in range(10):
	print(random.randrange(25, 36))'''

# The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths 
# of the other two sides. Look through the math module and see if you can find a function that will compute this 
# relationship for you. Once you find it, write a short program to try it out.
'''import math
import random

a = 5
b = 8

#print(math.hypot(a, b))

c = ([random.random(), random.random()], [random.random(), random.random()])

for a,b in c:
	print(math.hypot(a, b))'''



# Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. 
# Write a program to compute the approximation and then print that value as well as the value of math.pi from the 
# math module.

import math

print(f'The real value of pi is: {math.pi}')
print(f'The estimated value of pi is: {104348/33215}')

