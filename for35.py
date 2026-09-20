n = int(input('Введите значение n: '))
a1 = 3
a2 = 2
a3 = 1
if n>0:
    print(1,"   ")
    print(2,"   ")
    print(3,"   ")
    for i in range(4, n+1):
        ak = a1 + a2 - 2*a3
        print(ak)
        a1 = a2
        a2 = a3
        a3 = ak

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 10:44