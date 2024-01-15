def dispercy(array):  
    # Получаем количество элементов ряда
    n = len(array) 
    # Расчитываем среднее
    avg = sum(array) / n
    # Для каждого элемента рассчитываем отклонение как квадрат разности со средним
    deviations = [(x - avg) ** 2 for x in array] 
    # Суммируем, делим на количество элементов — получаем дисперсию
    dispercy = sum(deviations) / n 
    return dispercy

# a
rowA_1 = [2, 3, 7]
rowA_2 = [1, 2, 3]
# __23___7__
# _123______
print(dispercy(rowA_1), dispercy(rowA_2)) #4.6 и 0.6
# Для первого набора дисперсия больше

# б
rowB_1 = [2, 3, 4, 7]
rowB_2 = [1, 5, 6, 8]
# __234__7__
# _1___56_8_
print(dispercy(rowB_1), dispercy(rowB_2)) #3.6 и 6.5
# Для второго набора дисперсия больше