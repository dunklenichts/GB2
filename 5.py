'''
    Напишите программу для. проверки истинности утверждения
    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
from random import randint

x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)

first_stmnt = not (x or y or z)
second_stmnt = not x and not y and not z
result = first_stmnt == second_stmnt
print(f'x = {x}, y = {y}, z = {z}\nThe result is: {result}')
