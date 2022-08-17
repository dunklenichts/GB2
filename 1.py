'''
    Напишите программу, которая принимает на вход цифру, обозначающую день недели,
    и проверяет, является ли этот день выходным.
'''

input = input("Enter a day of week: ")

if input.isdigit():
    input = int(input)
    if any([1 <= input <= 5, 8 <= input <= 13, 15 <= input <= 19,
        22 <= input <= 26, 29 <= input <= 31]):
        print("No, this isn't a weeken")
    elif (input > 31):
        print('August has only 1 - 31 days :)')
    else:
        print("Yes, this is a weekend")
else:
    print('Enter an integer number')