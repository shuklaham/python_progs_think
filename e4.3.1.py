from swampy.TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()
#bob.delay = 0.01

'''
def square(t,l):
	for i in range(4):
		fd(t, l)
		lt(t)

square(bob,30)
'''

def polygon(t,l,n):
	angle = 360/n
	for i in range(n):
		fd(t, l)
		lt(t,angle)

#polygon(bob,100,6,60)


def circle(t, r):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n
	polygon(t, length, n)

circle(bob,60)

wait_for_user()