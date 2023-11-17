array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8, 9]
array1_prefix = [0,] * (len(array2) - len(array1))
array2_prefix = [0,] * (len(array1) - len(array2))
result = list(map(lambda x,y : x + y, array1_prefix + array1, array2_prefix + array2))
print(result)