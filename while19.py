import random
N = int(input('Введите значение N: '))
S = 0
q = N
while q>= 1:
    r =q%10
    S = S*10 +r
    q = int(q/10)
    print(S)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 17:37