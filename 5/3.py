string1 = input()
string2 = input()
set1 = set()
for symbol in string1:
	if(symbol != " "):
		set1.add(symbol)
set2 = set()
for symbol in string2:
	if(symbol != " "):
		set2.add(symbol)

result = 'Строки не являются анаграммами'
if(len(set1) == len(set2) and set1 == set2):
	result = 'Строки являются анаграммами'
print(result)