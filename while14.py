import random
a = float(input('Введите значение a: '))
k = 1.0
total = 1.0
t = 1.0
while total+1/(k+1) < a:
    k+=1
    t = 1/k
    total+=1/k
    print('Сумма: ', total)
    print('Наибольшее число: ', k)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 15:46