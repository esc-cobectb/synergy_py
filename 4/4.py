print("Введите строку из латинских букв:")
string = input()
print("Введите симвод для удвоения:")
char = input()
result = string.replace(char, char * 2)
print(result)