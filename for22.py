n = int(input('Введите значение n: '))
x = int(input('Введите значение x: '))
total = 1.0
num= 1.0
for i in range(1, n+1):
    num *= x/i
    total += num
print(total)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 19.09.26 11:43