def checkio(string):
	words = string.split(" ")
	count = 0
	check = False
	
	for word in words:
		if word.isalpha():
			count += 1
		elif word.isdigit():
			if not count >= 3:
				count = 0
	
	if count >= 3:
		check = True
	
	return check