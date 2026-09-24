eps = float(input('Введите значение eps: '))
A_prev = 2.0
A_curr = 2.0 + 1.0 / A_prev
k = 2
while abs(A_curr - A_prev) >= eps:
    A_prev = A_curr
    A_curr = 2.0 + 1.0 / A_prev
    k += 1
print(k, A_prev, A_curr)

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 21:40