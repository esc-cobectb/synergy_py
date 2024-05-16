import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

# И ещё раз оборачиваем повторяющуюся часть в функцию
def test (control_conversion, experiment_conversion):
    # Создадим DataFrame из данных
    data = pd.DataFrame({
        'group': ['control'] * 100 + ['experiment'] * 100,
        'conversion': np.concatenate([control_conversion, experiment_conversion])
    })

    # Проведем t-тест для проверки статистической значимости различий между группами
    control_data = data[data['group'] == 'control']['conversion']
    experiment_data = data[data['group'] == 'experiment']['conversion']
    t_stat, p_value = stats.ttest_ind(control_data, experiment_data)

    # Выведем результаты теста
    print(f"t-статистика: {t_stat:.4f}")
    print(f"p-значение: {p_value:.4f}")

    # Примем решение на основе p-значения
    alpha = 0.05
    if p_value < alpha:
        print("Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.")
    else:
        print("Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.")

# Создадим искусственные данные о конверсии
np.random.seed(1)
control_conversion = np.random.binomial(n=1, p=0.1, size=100)
# У экспериментальной группы вероятность конверсионного действия на 20% выше, чем у контрольной
experiment_conversion = np.random.binomial(n=1, p=0.12, size=100)

# Проверяем различия с помощью T-теста
test(control_conversion, experiment_conversion)
# t-статистика: -0.8677
# p-значение: 0.3866
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# Попробуем ещё раз на другом посеве
np.random.seed(6)
control_conversion = np.random.binomial(n=1, p=0.1, size=100)
# И для экспериментальной группы повысим вероятность конверсионного действия с 12% до 18%
experiment_conversion = np.random.binomial(n=1, p=0.18, size=100)
test(control_conversion, experiment_conversion)
# t-статистика: -1.7453
# p-значение: 0.0825
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# И ещё раз на третьем посеве
np.random.seed(9)
control_conversion = np.random.binomial(n=1, p=0.1, size=100)
# И для экспериментальной группы повысим вероятность конверсионного действия с 18% до 22%
experiment_conversion = np.random.binomial(n=1, p=0.22, size=100)
test(control_conversion, experiment_conversion)

# t-статистика: -2.9031
# p-значение: 0.0041
# Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.