y1= int(input('Координата y1: '))
y2= int(input('Координата y2: '))
y3= int(input('Координата y3: '))
x1= int(input('Координата x1: '))
x2= int(input('Координата x2: '))
x3= int(input('Координата x3: '))
import math
a= math.sqrt ((x3-x2)**2 + (y3-y2)**2)
print('Сторона a: ', a)
b= math.sqrt ((x3-x1)**2 + (y3-y1)**2)
print('Сторона b: ', b)
c= math.sqrt ((x2-x1)**2 + (y2-y1)**2)
print('Сторона c: ', c)
P= a+b+c
print('Периметр: ', P)
p= a+b+c/2
print('Полупериметр:  ', p)
S= math.sqrt (p*(p-a)*(p-b)*(p-c))
print('Площадь: ', S)
pass
#ФИО: Цветкова Полина Анатольевна 
#Дата и время выполнения: 13.09.26 14:24