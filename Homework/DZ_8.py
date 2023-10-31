# Файл 12, номер 5 (в,д)
"""
Написати функцію, яка за цілим числом визначає:
в) кількість входжень заданої цифри в його десятковий запис;
д) мінімальну (максимальну) цифру його десяткового запису.
"""
def findValue(num: int, value: int) -> int:
    num = str(num)
    value = str(value)
    counter = 0
    for i in num:
        if value == i:
            counter += 1
    print(counter)

def findMinMax(num: int) -> int:
    num = str(num)
    max = num[0]
    index = 0
    while index < len(num):
        temp = num[index]
        if max<temp:
            max = temp
        index += 1
    print(max)

findMinMax(-1233208572)
findValue(-122222227, 2)

# Файл 12, номер 13 
"""
Написати нерекурсивну функцію, яка за заданим n визначає число, що утворюється оберненням
десяткового запису n. Наприклад, оберненням 123 є 321, 340 — 43 (незначущі нулі відкидаються).
"""

def reverse(n):
    if n < 0:
        print (-1)
        return -1
    n = str(n)
    copy = n[::-1]
    copy = int(copy)
    print(copy)

reverse(12310)

# Файл 12, номер 16
"""
Написати функцію, яка за заданими дійсними a, h та цілим m друкує значення функції arctg(sin x) у
точках a, a+h, ..., a+mh.
"""

from math import sin, atan

def calc(a: float, h: float, m: int) -> float:
    
    index = 0
    while index <= m:
        result = atan(sin(a + h * index))
        index += 1
        print (f"For {a = }, {h = }, {m = }: {result = }")

calc(5, 5, 5)