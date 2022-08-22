'''
    Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
'''

input = input('Enter a number: ')
mult = 1

if input.isdigit() == True:
    input = int(input)
    for element in range(1, input+1):
        mult *= element
    print(f'The multiplication = {mult}')
else:
    print('Enter a valid number')

