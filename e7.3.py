import math
def test_square_root(a,x):
	epsilon = 0.0000001
	while True:
		#print x
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:
			break
		x = y

	print a,
	print x,
	print math.sqrt(a),
	print abs(math.sqrt(a)-x)

n=1.0
while n <=9.0 :
	test_square_root(n,n/2)
	n = n+1