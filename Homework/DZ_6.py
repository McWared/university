# Файл 8, номер 5 (перероблений)

import math

def a_check (a):

    if a==0:
        raise ValueError

def discriminant_check (discriminant):
    if discriminant < 0:
        raise ValueError("There is no roots, D < 0!")


def main ():

    try:
        a = float(input("a = "))
        a_check(a)
        b = float(input("b = "))
        c = float(input("c = "))

    except ValueError:
        print ("You aren`t allowed to input 0!")

    try:
        discriminant = (b ** 2) -4 * a * c
        discriminant_check(discriminant)

        x1 = (-b + math.sqrt(discriminant)) / 2 * a
        x2 = (-b - math.sqrt(discriminant)) / 2 * a
    except ValueError as e:
        print("There is a problem -", e)
    else:
        print (f"The equation is - {a}x^2 + {b}x + {c} = 0")
        print (f"{x1 = }")
        print (f"{x2 = }")

main()