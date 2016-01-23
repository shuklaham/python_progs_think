import math
def estimate_pi():
	k=0
	sum = 0	
	while True:
		expression = math.factorial(4*k)*(1103+26390*k)/(math.pow(math.factorial(k),4)*math.pow(396,4*k))
		if expression < 1e-15:
			break
		sum = sum + expression
		k = k +1
	pi_value = 1/(2*math.sqrt(2)/9801*sum)
	print pi_value

estimate_pi()
print math.pi
