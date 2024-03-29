import pandas as pd

d = ['a', 'b', 'c', 'd', 'e']
index = [0, 1, 2, 2, 4]
series = pd.Series(data = d, index = index)
# При создании объекта Series, где в индексе есть повторяющиеся элементы, на первый взгляд кажется, что элементы с повторяющимся индексом должны замещать друг друга
print(series)
# На деле объект имеет вполне себе полный исходный вид
# 0    a
# 1    b
# 2    c
# 2    d
# 4    e
# dtype: object
# При попытке получить значение по индексу, если он не повторяется, ожидаемо получаем значение.
print(series[1])
# Однако, при попытке получить значение по повторяющемуся индексу возвращается объект, содержащий все записи с повторяющимся индексом
print(series[2])
# 2    c
# 2    d
# dtype: object
# Аналогичная история с доступом по метке, соответствующей индексу через loc
print(series.loc[2])
# Доступо по индексу местоположения (по порядку) работает как ожидается, возвращает значение.
print(series.iloc[2])
print(series.iloc[3])
