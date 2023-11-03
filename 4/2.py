stringLen = 0
while(stringLen < 15):
	print("Введите строку не менее 15 символов:")
	string = input()
	stringLen = len(string)
	if(stringLen >= 15):
		break
	print('Строка слишком короткая, её длина', stringLen,' символов. Длина строки должна быть не менее 15 символов')

seq = string[::2]
print(seq)