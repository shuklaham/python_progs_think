def capitalize_all(t):
	res = ''
	for s in t:
		res= res+ s.capitalize()
	return res

print capitalize_all(raw_input());
