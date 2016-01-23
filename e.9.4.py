def uses_only(word,allowed):
	flag = 1
	for char in word:
		if char not in allowed:
			flag = 0
			break;
	if flag == 1:
		print True
	else:
		print False

uses_only('aaaaaeeeeeee','af')