# Файл 11, номер 2

def f(a:int):
    
    if a < 0:
        return -1
    n = 0
    factor = 1
    while factor < a:
        n += 1
        factor *= n
    return n, factor

n, factor = f(121)

print((n, factor))

# Файл 11, номер 20

import math

def func(a, b, h):

    for i in range (a, b+1, h):
        print(f"For {i = } result = {math.sin(i)}")

a = 1
b = 20
h = 2

func(a,b,h)

# Файл 12, номер 9

def sir (m:int) -> int:

    f2, f1 = 0, 1

    while f1 < m:
        f2, f1 = f1, f1 + f2
    print(f1)

sir(9)