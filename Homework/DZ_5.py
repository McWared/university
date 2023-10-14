# Файл 8, номер 5

def a_check (a):

    if a==0:
        raise ValueError

def coefficients (a, b, c):

    try:
        a = float(input("a = "))
        a_check(a)
        b = float(input("b = "))
        c = float(input("c = "))

    except ValueError:
        print ("You aren`t allowed to input 0!")

    else:
        print (f"{a}x^2 + {b}x + {c}")

coefficients(1,1,1)

# Файл 8, номер 9

import math

def x_check(x):
    if x < 0:
        raise ValueError("'x' must be greater then 0")

def root(x):

    try:
        x = float(input("x = "))
        x_check(x)
        result = math.sqrt(x)
    except ValueError as e:
        print ("Here is a problem -", e)
    else:
        print ("Result =", result)

root(1)

# Файл 8, номер 11

def variables_check (side1, side2, side3):
    if side1 < 0:
        raise ValueError("side`s lenght must be positive")
    if side2 < 0:
        raise ValueError("side`s lenght must be positive")
    if side3 < 0:
        raise ValueError("side`s lenght must be positive")
    
def side_check (side1, side2, side3):
    if (side1 + side2) <= side3:
        raise ValueError("Triangle doesnt exist")
    if (side1 + side3) <= side2:
        raise ValueError("Triangle doesnt exist")
    if (side2 + side3) <= side1:
        raise ValueError("triangle doesnt exist")

    
def triangle_area (side1, side2, side3):

    try:
        side1 = float(input("Side 1 = "))
        side2 = float(input("Side 2 = "))
        side3 = float(input("Side 3 = "))
        variables_check (side1, side2, side3)
        side_check(side1, side2, side3)

        p = (side1 + side2 + side3) / 2
        area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

    except ValueError as e:
        print ("Here is the problem -", e)

    else:
        print ("Area of this triangle =", area)

triangle_area(1, 1, 1)