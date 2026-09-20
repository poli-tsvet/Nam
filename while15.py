import random
P = float (input('Введите значение P: '))
S1 = 1000
S_end = 1100
coef = 1+P/100
print('Начальная цена = {0} Процент = {1}  coef = {2} '.format(S1,P,coef))
K = 0
S = S_end
while S<S_end:
    S *= coef
    K+=1
    print('K = {0}  S= {1} '.format(K,S))
    print('Месяца = {0}  Финальная цена = {1} '.format(K,S_end))

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 16:53