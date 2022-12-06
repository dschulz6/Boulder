"""Python Interpreter and Basics Exercise.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print (type(pi))
print (pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
	print ("sorry i = " + str(i) + " so it's less than 50")
else:	
	print ("Lucky you, i = " + str(i) + " so it was greater than 50 ")	


# TODO: Write a conditional that prints the color of the selected sportsball
picked_sportsball = random.choice(['tennis', 'basket', 'golf'])

print ("The sports ball that was picked for you was a " + str(picked_sportsball) + "ball ")
if picked_sportsball == "tennis":
	print ("A tennis ball is yellow")
elif picked_sportsball == "basket":
	print ("A basketball is orange")
elif picked_sportsball == "golf":
	print ("A golf ball is white")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multi(x,y):
	return x * y

# TODO: Now call the function a few times to calculate the following answers
#
# Entry point for program
if __name__ == '__main__':
	answer = multi(12,96)
	print ("Your numbers are 12 and 96")
	print("12 x 96 =", + answer)
	answer = multi(48,17)
	print ("Your numbers are 48 and 17")
	print("48 x 17 =", + answer)
	answer = multi(196523,87323)
	print ("Your numbers are 196523 and 87323")
	print("196523 x 87323 =", + answer)
