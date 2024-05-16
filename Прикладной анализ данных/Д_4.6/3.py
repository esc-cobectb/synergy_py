import numpy as np
import pandas as pd
# Со statsmodels пришлось повозиться, чтобы заработало, нужно было ставить с GitHub https://github.com/statsmodels/statsmodels
import statsmodels.api as sm

# И уже по классической схеме оборачиваем повторяющуюся часть в функцию
def test (control_group, experiment_group):
    # Создадим DataFrame из данных
    data = pd.DataFrame({
        'group': ['control'] * 100 + ['experiment'] * 100,
        'metric': np.concatenate([control_group, experiment_group])
    })
    # ANOVA — двусторонний дисперсионный анализ 
    # Проведем ANOVA для проверки статистической значимости различий между группами
    model = sm.formula.ols('metric ~ group', data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)

# Создадим искусственные данные с посевом 0
np.random.seed(0)
control_group = np.random.normal(loc=10, scale=3, size=100)
experiment_group = np.random.normal(loc=12, scale=3, size=100)

# Проводим ANOVA 
test (control_group, experiment_group)
#                sum_sq     df          F    PR(>F)
# group      213.544850    1.0  22.517597  0.000004
# Residual  1877.726173  198.0        NaN       NaN

# p-значение в данном случае 0.000004, то есть ниже уровня 0.05, что говорит нам о том, что в группах наблюдаюся статичтически значимые различия

# Теперь для эксперимента создадим другой набор с посевом 4
np.random.seed(4)
# Подвинем среднее значение распределения экспериментальной группы поближе к тестовой с 12 до 10.8
control_group = np.random.normal(loc=10, scale=3, size=100)
experiment_group = np.random.normal(loc=10.8, scale=3, size=100)
test (control_group, experiment_group)
#                sum_sq     df        F    PR(>F)
# group       28.849879    1.0  3.48886  0.063261
# Residual  1637.289920  198.0      NaN       NaN

# p-значение в данном случае 0.063261, что уже выше уровня 0.05, а значит группах не наблюдаюся статичтически значимые различия