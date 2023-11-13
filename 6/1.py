def isPalindrome(string):
	string = string.lower()
	stringArray = string.split()
	stringWithoutSpaces = "".join(stringArray)
	if(stringWithoutSpaces == stringWithoutSpaces[::-1]):
		return True
	else :
		return False

print(isPalindrome(input()))