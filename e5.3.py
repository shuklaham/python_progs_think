import math
def check_fermat(a,b,c,n):
	if n > 2 and ((math.pow(a,n)+ math.pow(b.n)) == math.pow(c,n)) :
		print "Holy Smokes, Fermat was Wrong"
	else:
		print "No, that doesn't work"

print "Type your 1st number - a \n"
first_num = int(raw_input())
print "Type your 2nd number - b \n"
sec_num = int(raw_input())
print "Type your 3rd number - c \n"
third_num = int(raw_input())
print "Type your power number - n \n"
raise_num = int(raw_input())

check_fermat(first_num,sec_num,third_num,raise_num)