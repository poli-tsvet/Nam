num= 1
a= int(input('Введите цену за 0.1 кг конфет: '))
for i in range(1, 11):
    num= i* 0.1
    b= a*num
    print(f'цена за {round(num, 2)} кг= {round(b, 2)} ')
    num+= 1
