print("Введите натуральные числа через пробел и последним числом степень:")
array = input().split()
power = array[-1]
nums = array[:-1]
squares = [int(i) ** int(power) for i in nums]
print(squares)
