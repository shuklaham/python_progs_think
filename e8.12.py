def rotate_word(s,num):
	temp = ''
	for c in s:
		increment = ord(c) + num
		if(increment>122):
			increment = (increment - 122) + (97 -1)
		temp = temp + chr(increment)
		#print temp
	return temp

print rotate_word('jolly',7)