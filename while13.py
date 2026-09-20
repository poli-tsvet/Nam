import random
a = float(input('Введите значение a: '))
k = 1.0
total = 1.0
t = 1.0
while total <= a:
    k+= 1
    t = 1/k
    total += 1/k
    print('Сумма: ',total)
    print('Наименьшее число: ', k)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 15:32