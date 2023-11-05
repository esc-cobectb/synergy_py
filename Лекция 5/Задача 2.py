n = int(input())
s = input()
delta = n - len(s)
k = delta // 2
p = delta % 2
result = s[0] * k + s + s[-1] * k
if(p > 0):
	result += '.'
print(result)