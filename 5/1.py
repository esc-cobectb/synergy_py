n = int(input())
cities = dict()
counter = 0
for i in range(0,n):
	city = input()
	if(city in cities):
		cities[city] += 1
	else :
		cities[city] = 1

duplicates = list(filter(lambda x: cities[x] > 1, cities))
for k in duplicates:
	counter += cities[k]
print(counter)