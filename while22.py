N = int(input('Введите значение N: '))
is_prime = True
i = 2
while i*i <= N:
    if N % i == 0:
        is_prime = False
    i += 1
    print(is_prime)
        

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 18:19