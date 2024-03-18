#   - Сгенерируйте 10 случайных чисел из каждого распределения.

import scipy.stats as sps
import matplotlib.pyplot as plt

def show_chart(sample, title, index):
	plt.subplot(3,2,index)
	plt.hist(sample, bins=20)
	plt.title(title)


def show_line(sample, title, index):
	plt.subplot(3,2,index)
	plt.plot(sample,  bins=20)
	plt.title(title)

#   - Создайте объекты распределений для нормального и равномерного распределений.
sample_norm = sps.norm.rvs(size=5000)
sample_uniform = sps.uniform.rvs(size=5000)

#   - Получите значения функции плотности вероятности (PDF) для каждого распределения при различных значениях.
pdf_norm = sps.norm.pdf(sample_norm)
print(pdf_norm)

pdf_uniform = sps.uniform.pdf(sample_uniform)
print(pdf_uniform)

#   - Получите значения функции кумулятивной вероятности (CDF) для каждого распределения при различных значениях.
cdf_norm = sps.norm.cdf(sample_norm)
print(cdf_norm)

cdf_uniform = sps.uniform.cdf(sample_uniform)
print(cdf_uniform)

# Это для теста, что распределения у нас нагенерировались такие, какие мы хотели
plt.figure(figsize=(10,8))
show_chart(sample_norm, 'Нормальное распределение', 1)
show_chart(sample_uniform, 'Равномерное распределение', 2)

# show_chart(pdf_norm, 'PDF Нормальное распределение', 3)
show_line(pdf_norm, 'PDF Нормальное распределение', 3)
show_chart(pdf_uniform, 'PDF Равномерное распределение', 4)

show_chart(cdf_norm, 'CDF Нормальное распределение', 5)
show_chart(cdf_uniform, 'CDF Равномерное распределение', 6)

plt.show()
