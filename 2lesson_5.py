'''
    Реализуйте алгоритм перемешивания списка.
'''
import random
from random import randint

list = []
for elem in range(10):
    list.append(randint(0, 10))
print(f'source list is {list}')

for elem in range(len(list)):
    rand_index = randint(0, 9)
    temp = list[elem]
    list[elem] = list[rand_index]
    list[rand_index] = temp
print(f'the list after combination is {list}')
