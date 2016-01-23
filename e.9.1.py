fin = open('words.txt')
for line in fin:
	#previous_length = len(line)
	word = line.strip()
	if(len(word) <20):
		print word