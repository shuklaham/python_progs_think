def is_abcderian(word):
	#l = len(word);
	i = 0
	while (i<=len(word)-2):
		if ord(word[i+1]) < ord(word[i]):
			return False
		i=i+1
	return True

print is_abcderian('aaaaabcdef')
print is_abcderian('aaaaabcdefaa')