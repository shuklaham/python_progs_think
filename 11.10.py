def rotate_word(s,num):
	temp = ''
	for c in s:
		increment = ord(c) + num
		if(increment>122):
			increment = (increment - 122) + (97 -1)
		temp = temp + chr(increment)
		#print temp
	return temp

def rotate_pairs(w1,w2):
    diff = []
    if len(w1) != len(w2):
        return False
    lw1 = list(w1)
    lw2 = list(w2)
    for i in range(len(lw1)):
        s = ord(lw1[i]) - ord(lw2[i])
        diff.append(s)
    return checkEqual2(diff)


def checkEqual2(iterator):
    return len(set(iterator)) <= 1

fin = open('words.txt')
for line1 in fin:
    for line2 in fin:
        if line1 == line2:
            continue
        if rotate_pairs(line1,line2):
            print line1, line2
