# Функция поиска медианы
def median(array):
	#Сортируем массив чисел
    sorted_array = sorted(array)
    # Получаем количество элементов в массиве
    array_len = len(sorted_array)
    # Расчитываем индекс середины
    middle = (array_len - 1) // 2
    # Если индекс нечетный, то медиана - значение элемента по этому индексу
    if middle % 2:
        return sorted_array[middle]
    else:
    # Если индекс четный, то берем среднее между двумя соседними средними элементами
        return (sorted_array[middle] + sorted_array[middle + 1]) / 2.0

# Функция вычесления среднего арифметического
def avg(array):
	return sum(array) / len(array)

rowB = [18.0, 17.1, 15.3, 13.1, 14.9]
rowV = [17.8, 12.9, 14.4, 15.6, 19.4]
rowA = rowB + rowV

#a
print(median(rowA), avg(rowA)) # Медиана 15.45, Средняя урожайность 15.85
print(median(rowA) - avg(rowA)) # Медиана ниже среднего на 0.4
#б
print(median(rowB), avg(rowB)) # Медиана 16.2, Средняя урожайность 15.68
print(median(rowB) - avg(rowB)) # Медиана выше среднего на 0.52
#в
print(median(rowV), avg(rowV)) # Медиана 16.7, Средняя урожайность 16.02
print(median(rowV) - avg(rowV)) # Медиана выше среднего на 0.67