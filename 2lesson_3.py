'''
    Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
'''

input = input('Enter number: ')
i = 1

if input.isdigit() == True:
    input = int(input)
    for element in range(1, input + 1):
        output = round(((1 + 1 / i) ** i), 2)
        i += 1
print(f'The output of convergent series is {output}')