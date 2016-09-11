def reverse(text):
	index = len(text) - 1
	string = []
	while index >= 0:
	    string.append(text[index])
	    index -= 1
	return ''.join(string)
	    
print reverse('Python!')

