print("Введите строку:")
string = input()
x = 0
y = 0
for i in string:
	if(i == 'x'):
		x += 1
	if(i == 'y'):
		y += 1
print('x:',x,', y:', y)