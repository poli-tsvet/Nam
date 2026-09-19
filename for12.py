n= int(input("Введите значение n: "))
total = 1
for i in range(1, n + 1):
    b= (i/10) + 1
    total = total *b

print(f"Произведение чисел {round(total,2)}")

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 16.09.26 17:01