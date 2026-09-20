x = float(input('Введите значение x: '))
n = int(input('Введите значение n: '))
total = x
num = x
k = 1
for i in range(1, n + 1):
    k += 2
    num *= -1 * (x*x)
    total += num/k
print('Значение выражения: ', total)
# ФИО: Цветкова Полина Анатольевна
# Дата и время: 19.09.26 15:05