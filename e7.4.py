import math
def eval_loop():
	ans = "Not really interested"
	while True:
		print ">",
		s = raw_input()
		if s == "done":
			break
		ans = eval(s)
		print ans
	print ans

'''
This is really important technique. See line 3.
'''
eval_loop()