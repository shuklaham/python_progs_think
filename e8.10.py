def is_palindrome(str):
	if(str[:len(str)/2:1] == str[:len(str)/2-1:-1]):
		print 'Yes'
	else:
		print 'No'

is_palindrome('pooja')
is_palindrome('poop')