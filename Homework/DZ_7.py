# Файл 11, номер 2
"""
Написати рекурсивну функцію, яка за цілим числом визначає кількість входжень заданої цифри в його десятковий запис.
"""

def find_number(value, numToFind):

    if value<=0:
        return 0
    
    if value % 10 == numToFind:
        return 1 + find_number(value // 10, numToFind)
    else:
        return find_number(value // 10, numToFind)
    
print(find_number(123456654321, 6)) # Output: 2 (correct)

# Файл 11, номер 10

"""
Написати рекурсивну функцію обчислення числа Фібоначчі.
"""

counter = 0

def fib(num):

    global counter
    counter += 1

    if num<0:
        return -1
    if num==0:
        return 0
    if num==1:
        return 1
    
    return fib(num - 1) + fib(num - 2)

print(fib(20)) # Output: 8 (correct)
print(counter)
