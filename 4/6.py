print("Введите строку:")
string = input()
start = 0
bracketStart = 0
bracketeEnd = 0
while True:
	bracketStart = string.find('(', start)
	bracketeEnd = string.find(')',start)
	if(bracketStart > -1 and bracketeEnd > -1):
		print(string[bracketStart+1:bracketeEnd])
		start = bracketeEnd + 1
	else :
		break
