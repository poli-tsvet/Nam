num = 1
a= int(input('Введите цену за 1.2 кг: '))
for i in range (12, 21):
    num = i * 0.1
    b= a* num
    print(f'Цена за {round(num, 2)} кг = {round(b, 2)}')
    num+= 1