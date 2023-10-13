# Тернарні оператори

x = int(input("x = "))

a = 0 if x < 0 else 1

print(a)

# Повнотекстові матеріали, файл 6, завд. 11

from math import e, pi

def sum (x, y):
    result = (x + pi)/(x**2 + y**4 + e)
    print ("Result =", result)

sum(x = float(input("x = ")), y = float(input("y = ")))

# Завд. 18

def module (a, x):
    result = abs(x**5 + abs(a * x - x**3) - a) + a * x**2 + a**8
    return result

print(module(a = float(input("a = ")), x = float(input("x = "))))

# Файл 7, завд. 39

def rah(x, y):
    if x > 3:
        z = x + y
    elif x <= 0:
        z = x - y
    else:
        z = x + 2
    return z

print(rah(x = float(input("x = ")), y = float(input("y = "))))