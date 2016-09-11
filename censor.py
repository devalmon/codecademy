def censor(text, word):
	censoredText = text
	if word in text:
		censoredText = censoredText.replace(word, "*" * len(word))
	return censoredText
		
print censor("this hack is wack hack", "hack") 
