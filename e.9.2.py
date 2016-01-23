def has_no_e(word):
	for char in word:
		if char =='e':
			return False
	return True

total_count = 0
ewords_count = 0
fin = open('words.txt')
for line in fin:
	word = line.strip()
	total_count = total_count +1
	if has_no_e(word) == True:
		print word
		ewords_count = ewords_count +1
print ewords_count/total_count*100




