n = int(input('Введите значение n: '))
fact = 1.0
total = 1.0
for i in range(1, n +1):
    fact *= i
    total += 1.0/ fact
print(total)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 19.09.26 11:35