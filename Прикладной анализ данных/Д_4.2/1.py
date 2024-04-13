import pandas as pd
import matplotlib.pyplot as plt
# Форматер для дат, а то они по-буржуйски не читаются
import matplotlib.dates as mdates

df = pd.read_csv('supermarket_sales.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Постройте график общего объема продаж по дням/месяцам/годам. Какие тенденции или сезонные всплески можно выявить на графике?
width = 1
frame = df.groupby(['Date']).agg({'Total': ['sum']}).reset_index()
fig = plt.figure()
fig.canvas.manager.set_window_title('Объем продаж по дням')
plt.bar(x=frame['Date'], height=frame['Total']['sum'], width = width)
plt.title('Объем продаж по дням')
plt.xlabel('Дата')
plt.ylabel('Выручка ($)')
plt.xticks(rotation=90)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gca().xaxis_date()   
plt.grid(True)


width = 10
frame = df.groupby(pd.Grouper(freq="M",key="Date")).agg({'Total': ['sum']}).reset_index()
fig = plt.figure()
fig.canvas.manager.set_window_title('Объем продаж по месяцам')
plt.bar(x = frame['Date'], height=frame['Total']['sum'], width = width)
plt.title('Объем продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Выручка ($)')
plt.xticks(frame['Date'].values, rotation=90)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
plt.grid(True)

width = 1
frame = df.groupby(pd.Grouper(freq="Y",key="Date")).agg({'Total': ['sum']}).reset_index()
fig = plt.figure()
fig.canvas.manager.set_window_title('Объем продаж по годам')
plt.bar(x = frame['Date'], height=frame['Total']['sum'], width = width)
plt.title('Объем продаж по годам')
plt.xlabel('Год')
plt.ylabel('Выручка ($)')
plt.xticks(frame['Date'].values, rotation=90)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.grid(True)

# Период в данных оказался маловат - январь-март 2019 года
# Однако, по графикам можно понять, что наибольшая выручка была в Январе выше, чем в другие месяци, а в феврале — ниже. Хотя, этому может быть разумное объяснение, так как в январе 31 день, а в феврале 28.

# Выберите наиболее подходящий тип диаграммы для визуализации распределения цен на товары. Постройте эту диаграмму и определите с ее помощью, какие ценовые диапазоны наиболее популярны.
fig = plt.figure()
fig.canvas.manager.set_window_title('Ценовые диапазоны')
plt.hist(df['Unit price'], edgecolor = 'white', bins = 25)
# Судя по гистограмме на 25 диапазонов, самыми популярными являются от 71.2 до 74.6 доллара и от 96.6 до 100 долларов

# -------------------------------------------------------------------------------
# Тут я попытался выяснить какой вообще разброс цен по категориям и в какой категории берут товары в среднем подороже
# frame = df.groupby('Product line')['Unit price'].apply(list)
# fig = plt.figure()
# fig.canvas.manager.set_window_title('Распределение цен по категориям')
# plt.boxplot(frame)
# ticks = list(range(1, len(frame)+1))
# tickNames = frame.index.values
# plt.xticks(ticks, tickNames, rotation=90)
# Оказалось, что во всех категориях разброс цен плюс-минус одинаковый, но в среднем подороже товары берут в категории Sport and Travel
# Но не так, чтобы на этом можно было сделать какой-то полезный вывод
# -------------------------------------------------------------------------------
plt.show()

