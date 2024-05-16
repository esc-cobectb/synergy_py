import numpy as np
from scipy import stats

# Чтобы повести несколько экспериментов закинем основную часть оценки результатов в функцию
def calc (users_control, purchases_control, users_experiment, purchases_experiment):
    # Вычисляем конверсию для каждой группы
    conversion_control = purchases_control / users_control
    conversion_experiment = purchases_experiment / users_experiment

    # Проводим двухвыборочный z-тест
    z_stat, p_value = stats.ttest_ind_from_stats(mean1=conversion_control, std1=np.sqrt(conversion_control*(1-conversion_control)), nobs1=users_control,
                                                  mean2=conversion_experiment, std2=np.sqrt(conversion_experiment*(1-conversion_experiment)), nobs2=users_experiment)

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
users_control = 1000  # общее количество пользователей
purchases_control = 50  # количество пользователей, совершивших покупку

# Данные для экспериментальной группы (группа B)
users_experiment = 1100  # общее количество пользователей
purchases_experiment = 70  # количество пользователей, совершивших покупку

calc (users_control, purchases_control, users_experiment, purchases_experiment)
# Конверсия в контрольной группе: 0.0500
# Конверсия в экспериментальной группе: 0.0636
# p-значение: 0.1787
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# Теперь попробуем немного увеличить количество покупок в экспериментальной группе на 10%
purchases_experiment *= 1.1 
calc (users_control, purchases_control, users_experiment, purchases_experiment)
# Конверсия в контрольной группе: 0.0500
# Конверсия в экспериментальной группе: 0.0700
# p-значение: 0.0547
# Принимаем нулевую гипотезу: Нет статистически значимых различий между группами.

# Теперь накинем ещё 20%
purchases_experiment *= 1.2 
calc (users_control, purchases_control, users_experiment, purchases_experiment)
# Конверсия в контрольной группе: 0.0500
# Конверсия в экспериментальной группе: 0.0840
# p-значение: 0.0019
# Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами.

# Вот разница конверсий 5% и 8.4% в группах около 1000 человек уже является статистически значимой. 