A = int(input('Введите значение A: '))
B = int(input('Введите значение B: '))
C = int(input('Введите значение C: '))
count_A = 0
temp_A = A
while temp_A >= C:
    temp_A -= C
    count_A += 1
count_B = 0
temp_B = B
while temp_B >= C:
    temp_B -= C
    count_B += 1
total = 0
for i in range(count_B):
    total += count_A
print('Всего квадратов: ',total)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 22:01