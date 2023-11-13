def maxOfNumbers(arg1, arg2, arg3 = 0):
	return max(arg1, arg2, arg3)

args = list(map(int, input().split()))
if(len(args) == 3):
	print(maxOfNumbers(args[0], args[1], args[2]))
elif (len(args) == 2):
	print(maxOfNumbers(args[0], args[1]))