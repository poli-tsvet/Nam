N = int(input('Введите значение N: '))
Flag = False
while N>0:
    if (N%10) %2 !=0:
        Flag = True
    N=N//10
    print(Flag)
        

# ФИО: Цветкова Полина Анатольевна
# Дата и время: 20.09.26 18:11