'''
    Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
    в одной строке одно число.
'''

from random import randint

input = input('Enter a range: ')
list = []

with open ("C:/Users/Desktop/txt.txt", "r", encoding="utf-8") as file: # text in file: 3 \n 5
    numbers = file.read().splitlines()
    file.close()

if input.isdigit() == True:
    input = int(input)
    a = -input                        # иначе генерит числа, первые из которых всегда == 0
    b = input
    for elem in range(input):
        list.append(randint(a, b))
    print(list)
    # print(list[0])

    x = int(numbers[0])
    y = int(numbers[1])

    mult = list[x - 1] * list[y - 1]
    print(mult)
else:
    print('Enter a valid number')
