import math
def square_root(x,a):
	epsilon = 0.00001
	while True:
		print x
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:
			break
		x = y
	print x

number = int(raw_input())
est = int(raw_input())
square_root(number,est)