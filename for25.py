x = float(input('Введите значение x: '))
n = int(input('Введите значение n: '))
total = x
num = x
for i in range(2, n+1):
    num *= -1 * x
    total += num/i
print('Значение выражения: ', total)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 19.09.26 14:48