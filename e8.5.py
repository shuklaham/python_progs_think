def count(str, letter):
	c = 0
	i = 0
	while i < len(str):
		if str[i] == letter:
			c = c + 1
		i = i + 1
	return c


iter = count('distance','i')
print iter
iter = count('miss','s')
print iter
