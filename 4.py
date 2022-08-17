'''
    Напишите программу, которая принимает на вход координаты двух точек и
    находит расстояние между ними в 2D пространстве.
'''
from math import sqrt

x1 = input('Enter coordinated of x1: ')
y1 = input('Enter coordinated of y1: ')
x2 = input('Enter coordinated of x2: ')
y2 = input('Enter coordinated of y2: ')

try:
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    output = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print(f'Distance between two dots is {output:.2f}')
except ValueError:
    print('Enter an integer number')
