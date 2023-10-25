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