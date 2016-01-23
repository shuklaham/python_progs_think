def avoids(word,forbidden):
	flag = 0
	for char in forbidden:
		#print char
		if(char in word):
			flag = 1
			#print 'e'
			break;
	if flag ==0:
		return 'Nothing forbidden'
		#print 'b'
	else:
		return 'Not allowed'
		#print 'g'

print 'Enter the word you wanna check ',
word_chk = raw_input()
print 'forbidden letters please ',
forbidden = raw_input()
print avoids(word_chk,forbidden)