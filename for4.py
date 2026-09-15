num= 1
a= int(input('Укажите стоимость конфет за 1 кг: '))
for i in range(1, 11):
    b= a*num
    print(f'цена за {round(num, 2)} кг = {round(b, 2)}')
    num += 1