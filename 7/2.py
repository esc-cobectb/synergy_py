array = [13,14,19,26,27,28,38,39,40]
result = list(filter(lambda x : x % 19 == 0 or x % 13 == 0, array))
print(result)