import numpy as np
from scipy import stats

# Тут та же самая история, что и в кейсе №4, но уже немного ООП. Соберём не функицю, а класс для тестирования.
class ABTest:
    def __init__(self, control_conversion_rate, experiment_conversion_rate, control_sample_size, experiment_sample_size):
        # Тут у нас свойства класса для контрольной группы
        self.control_conversion_rate = control_conversion_rate
        self.control_sample_size = control_sample_size
        # А тут свойства класса для экспериментально группы
        self.experiment_conversion_rate = experiment_conversion_rate
        self.experiment_sample_size = experiment_sample_size

    def simulate(self):
        # Генерируем случайные данные о конверсии
        control_conversion = np.random.binomial(n=1, p=self.control_conversion_rate, size=self.control_sample_size)
        experiment_conversion = np.random.binomial(n=1, p=self.experiment_conversion_rate, size=self.experiment_sample_size)

        # Проведение t-теста для сравнения конверсий
        t_stat, p_value = stats.ttest_ind(control_conversion, experiment_conversion)

        # Вывод результатов. Нужно побольше цифр после запятой, иначе p-значение иногда будет выглядеть как 0.0000 
        print(f"t-статистика: {t_stat:.6f}")
        print(f"p-значение: {p_value:.6f}")

        # Принятие решения на основе p-значения
        alpha = 0.05
        if p_value < alpha:
            print("Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.")
        else:
            print("Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.")

# Инициализируем класс для A/B-тестирования
test = ABTest(control_conversion_rate=0.1, experiment_conversion_rate=0.12, control_sample_size=1000, experiment_sample_size=1000)
# Тестируем
test.simulate()
# t-статистика: -0.4321
# p-значение: 0.6657
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# Поднимаем вероятность конверсионного действия в экспериментельной группе до 17% 
test.experiment_conversion_rate = 0.17
test.simulate()
# t-статистика: -2.474850
# p-значение: 0.013412
# Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.