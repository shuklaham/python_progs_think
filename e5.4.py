import math
def is_triangle(a,b,c):
	if (a > (b+c)) or (b > (a+c)) or (c > (b+a)):
		print "No"
	else:
		print "Yes"

print "Type your 1st side - a \n"
first_num = int(raw_input())
print "Type your 2nd side  - b \n"
sec_num = int(raw_input())
print "Type your 3rd side - c \n"
third_num = int(raw_input())

is_triangle(first_num,sec_num,third_num)