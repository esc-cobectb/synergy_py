print("Введите строку:")
string = input()
result = ''
start = 0
bracketStart = 0
bracketeEnd = 0
while True:
	bracketStart = string.find('(', start)
	bracketeEnd = string.find(')',start)
	if(bracketStart > -1 and bracketeEnd > -1):
		result += string[start:bracketStart-1]
		start = bracketeEnd + 1
	else :
		end = len(string)
		result += string[start:end]
		break
print(result)
# В задании ошибка контрольного примера.
# Из задания: ...программа выводит на экран текст без скобок и их содержимого
# Значит при вводе: When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!
# Должен быть вывод: When he saw Sally  in the shop, he could not believe his eyes. She was fantastic !
# А в конрольном примере наоборот, содержание скобок