import sys

name = sys.argv[1]

def right_justify(s) :
	print ' '*(70 - len(s))+s

right_justify(name)
