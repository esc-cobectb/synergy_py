def formatName(string):
	currentYear = 2023
	stringArray = string.split()
	age = int(stringArray[-1])
	year = currentYear - age
	stringArray[-1] = str(year)
	return " ".join(stringArray) + ' г.р. зарегистрирован'

print(formatName(input()))