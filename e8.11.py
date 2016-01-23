def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False

# Wrong. Return statement should not be used.

def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'
#Wrong. Cannot use 'c'

def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	return flag
# Wrong, dont use return

def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

# Right

def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False
	return True

# True

print any_lowercase5('shuBham');00000000000000