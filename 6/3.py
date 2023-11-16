def maxOfNumbers(arg1, arg2, arg3 = 0):
	if(arg1 >= arg2 and arg1 >= arg3):
		return arg1
	elif (arg2 >= arg1 and arg2 >= arg3):
		return arg2
	else :
		return arg3

args = list(map(int, input().split()))
if(len(args) == 3):
	print(maxOfNumbers(args[0], args[1], args[2]))
elif (len(args) == 2):
	print(maxOfNumbers(args[0], args[1]))