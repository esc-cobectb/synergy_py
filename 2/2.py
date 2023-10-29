print("Введите два числа через пробел:")
nums = list(map(int, input().split()))
if (nums[0] > nums[1]):
	result = nums[0]
else :
	result = nums[1]
print(result)