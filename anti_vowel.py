def anti_vowel(text):
	vowel = 'aeiouAEIOU'
	result = text
	for c in text:
		for l in vowel:
			if c == l:
				result = result.replace(c, '')
	
	return result

print anti_vowel('Hey You!')