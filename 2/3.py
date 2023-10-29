print("Клетка с координатами {1;1} левая нижняя и она черная.")
print("Введите координаты шахматной доски:")
nums = list(map(int, input().split()))
if (nums[0] > 8 or nums[1] > 8):
	result = 'Координаты за пределами шахматной доски 8x8'
else :
	if(nums[0] % 2 != 0 and nums[1] % 2 == 0):
		result = 'YES'
	elif(nums[0] % 2 == 0 and nums[1] % 2 != 0):
		result = 'YES'
	else:
		result = 'NO'
print(result)