def uses_all(word,allowed):
	for char in allowed:
		if char not in word:
			return False
	return True

print uses_all('shubham','sba')
print uses_all('shubhm','sba')
