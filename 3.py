'''
    Напишите программу, которая по заданному номеру четверти, показывает диапазон
    возможных координат точек в этой четверти (x и y).
'''

quarter_number = input('Enter a quarter number: ')

try:
    quarter_number = int(quarter_number)
    if quarter_number == 1:
        print('x > 0, y > 0')
    elif quarter_number == 2:
        print('x < 0, y > 0')
    elif quarter_number == 3:
        print('x < 0, y < 0')
    elif quarter_number == 4:
        print('x > 0, y < 0')
    else:
        print('Enter a number from 1 to 4')
except ValueError:
    print('Enter an integer number')