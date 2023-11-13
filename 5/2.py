text = input()
separators = [". ", "! ", "? "]
for s in separators:
	textArray = text.split(s)
	if(len(textArray)):
		for i,p in enumerate(textArray):
			words = p.split()
			if(len(words)):
				words[0] = words[0].title()
				textArray[i] = " ".join(words)	
	text = s.join(textArray)	
print(text)