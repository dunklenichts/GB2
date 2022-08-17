'''
    Напишите программу, которая принимает на вход координаты точки (X и Y),
    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
    эта точка (или на какой оси она находится).
'''

x = input('Enter x: ')
y = input('Enter y: ')

try:
    x = int(x)
    y = int(y)
    if (x > 0) and (y > 0):
        print('1 quarter')
    elif (x < 0) and (y < 0):
        print('3 quarter')
    elif (x > 0) and (y < 0):
        print('4 quarter')
    elif (x < 0) and (y > 0):
        print('2 quarter')
    elif (x == 0) or (y == 0):
        print('Enter coordinated != 0')
except ValueError:
    print('Enter an integer')