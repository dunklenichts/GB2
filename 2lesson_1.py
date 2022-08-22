'''
    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''

input = input('Enter a number: ')

sum = 0

for elem in input:
    if (elem != '.'):
        sum += int(elem)
print(sum)