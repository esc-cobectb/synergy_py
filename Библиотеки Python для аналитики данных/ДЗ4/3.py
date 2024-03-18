import pandas as pd

data = [i ** 2 for i in range(1,21)]
series = pd.Series(data = data)
# Весь объект
print(series)
seriesNot3 = series[series.index % 3 != 0]
# Только элементы, чьи индексы не делятся на 3
print(seriesNot3)
