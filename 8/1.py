def recursive_max(array):
	if(len(array) == 1):
		return array[0]
	else :
		last = array.pop()
		tail = recursive_max(array)
		return last if last >= tail else tail

array = [1, 9, 7, -17, 32, -2, 12, 55, 0, 2]
result = recursive_max(array)
print(result)