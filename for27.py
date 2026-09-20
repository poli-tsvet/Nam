x = float(input('Введите значение x: '))
n = int(input('Введите значение n: '))
total = x
num = x
for i in range(1, n + 1):
    num *= (x*x) *(2*i -1) 
    total += num/((2*i) * (2*i +1))
print('Значение выражения: ', total)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 19.09.26 22:23