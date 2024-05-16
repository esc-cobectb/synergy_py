import numpy as np
from scipy.stats import ttest_ind

# Как и в первом примере обернём расчетную часть в функцию
def calc(visits_control, conversions_control, visits_experiment, conversions_experiment):
    # Вычисляем конверсию для каждой группы
    conversion_control = conversions_control / visits_control
    conversion_experiment = conversions_experiment / visits_experiment

    # Проводим t-тест для сравнения средних значений конверсии между группами
    t_stat, p_value = ttest_ind([1] * conversions_control + [0] * (visits_control - conversions_control),[1] * conversions_experiment + [0] * (visits_experiment - conversions_experiment))

    # Выводим результаты
    print(f'Конверсия в контрольной группе: {conversion_control:.4f}')
    print(f'Конверсия в экспериментальной группе: {conversion_experiment:.4f}')
    print(f'p-значение: {p_value:.4f}')

    # Принимаем решение на основе p-значения
    alpha = 0.05
    if p_value < alpha:
        print("Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.")
    else:
        print("Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.")
    print('-'*20)

# Данные для контрольной группы (группа A)
visits_control = 2000  # количество посетителей контрольной страницы
conversions_control = 100  # количество пользователей, совершивших целевое действие на контрольной странице

# Данные для экспериментальной группы (группа B)
visits_experiment = 2200  # количество посетителей экспериментальной страницы
conversions_experiment = 120  # количество пользователей, совершивших целевое действие на экспериментальной странице

# Сравниваем контрольную и тестовую группы.
calc(visits_control, conversions_control, visits_experiment, conversions_experiment)
# Конверсия в контрольной группе: 0.0500
# Конверсия в экспериментальной группе: 0.0545
# p-значение: 0.5091
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# Давайте накинем немного целевых действий в конверсию экспериментальной группы, чтобы увидеть разницу. Например, 10%.
# Обязательно нужно перевести в целые, количество продаж не может быть дробным, да и python будет ругаться, если такое произойдёт.
conversions_experiment = (int) (conversions_experiment * 1.10)
calc(visits_control, conversions_control, visits_experiment, conversions_experiment)
# Конверсия в контрольной группе: 0.0500
# Конверсия в экспериментальной группе: 0.0627
# p-значение: 0.0748
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# И ещё 10%.
conversions_experiment = (int) (conversions_experiment * 1.10)
calc(visits_control, conversions_control, visits_experiment, conversions_experiment)
# Конверсия в контрольной группе: 0.0500
# Конверсия в экспериментальной группе: 0.0659
# p-значение: 0.0280
# Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.