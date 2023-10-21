# Файл 11, номер 2
"""
Написати рекурсивну функцію, яка за цілим числом визначає кількість входжень заданої цифри в його десятковий запис.
"""

def find_number(value):

    numToFind = int(input("Enter number to find (0,1,2,3,4,5,6,7,8,9): "))

    count = 0

    if value==0:
        return 
