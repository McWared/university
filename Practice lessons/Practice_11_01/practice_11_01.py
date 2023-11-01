# Файл 12, номер 36

"""
Знайти кількість п'ятизначних чисел, у десятковому запису яких є цифра b.
nums = [10000 - 99999] len(nums) = 90000
"""

# 1 спосіб

def find(b: int) -> int:
    
    counter = 0

    for i in range (10000, 100000):
        i, b = str(i), str(b)
        if b in i: counter += 1

    print(f"For {b}: {counter = }")

find(1)

# 2 спосіб

def findNumber(b: int, number: int) -> bool:
    return str(b) in str(number)

def calc(b: int) -> int:

    counter = 0
    for i in range(10000, 100000):
        if findNumber(b, i): counter += 1
    
    print(f"For {b}: {counter = }")

calc(1)

# 3 спосіб (без переводу в строки)

def findNumber2(b:int, number:int) -> bool:

    while number > 0:
        last_elem = number % 10
        if b == last_elem: return True
        number //= 10

    return False

def calc2(b: int) -> int:

    counter = 0
    for i in range(10000, 100000):
        if findNumber2(b, i): counter += 1
    
    print(f"For {b}: {counter = }")

calc2(1)