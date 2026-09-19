n= int(input("Введите значение n: "))
total = 0
sign = 1
for i in range(1, n + 1):
    b= (i*0.1) + 1
    total+=sign*b
    sign=-sign 

print(f"Значение выражений {round(total, 2)} ")

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 16.09.26 17:08
