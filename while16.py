import random
D = 10
Total = 100
P = float(input('Ведите значение P: '))
coef = 1+P/100
print('Первый день = {0}  Процент = {1}  Coef = {2} '.format(D,P,coef))
K = 1
S = D
while S<Total:
    D *= coef
    S += D
    K+=1
    print('K = {0}  D = {1}  S = {2} '.format(K,D,S)) 
    print('Days = {0} Summary ={1} '.format(K,S))

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 17:13