from functools import reduce
array = [1, 99, 13,14,19,26,27,28,105,38,39,40]
result = reduce(lambda x, y:  x if x > y else y, array)
print(result)