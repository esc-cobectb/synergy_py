import pandas as pd
# 1. Считайте данные из файла "students.csv" с помощью метода read_csv.
df = pd.read_csv('students.csv')
print(df)
# 2. Выведите первые 3 строки датафрейма с помощью метода head.
print(df.head(3))
# 3. Выведите последние 2 строки датафрейма с помощью метода tail.
print(df.tail(2))
# 4. Получите общую информацию о датафрейме с помощью метода info.
print(df.info())