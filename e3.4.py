def do_four(f,v):
	f(v)
	f(v)

def print_twice(v):
	print v
	print v

do_four(print_twice,'spam')


