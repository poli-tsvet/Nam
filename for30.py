import math
n = int(input('Введите значение n: '))
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
h = (b -a)/n
for i in range (1,n +1):
    print(a+i *h)
    print(a- math.sin(a+i*h))

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 19.09.26 23:12