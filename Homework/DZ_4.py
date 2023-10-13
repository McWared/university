# Файл 6 №5(а - г)

import math

# a)

def ln (a, b):
    return math.log (math.sqrt(a ** 2 + b ** 2))

print (ln (a = float (input ("a1 = ")), b = float (input ("b1 = "))))

# б)

def sinus (a, b):
    return (math.sin ((a + b) ** (1 / 7)))

print (sinus (a = float (input ("a2 = ")), b = float (input ("b2 = "))))

# в)

def cosinus (a, b):
    return (math.cos ((a ** 12 + b ** 12) ** (1/3)))

print (cosinus (a = float (input ("a3 = ")), b = float (input ("b3 = "))))

# г)

def ctg (a, b):
    return (math.cos (abs (math.sqrt (a) - math.sqrt(b))) / math.sin (abs (math.sqrt (a) - math.sqrt(b))))

print (ctg (a = float (input ("a4 = ")), b = float (input ("b4 = "))), "\n")

# Файл 7 № 10, 43, 45

# 10)

print("Номер 10", "\n")

x = 10
y = x
z = y

print (id (x) == id (y) == id (z))

'or'

print (x is y is z, "\n")

# 43)

print("Номер 43", "\n")

a = True

match a:
    case True: print ("Yes", "\n")
    case False: print ("No", "\n")
    case _: print ("Error:)", "\n")

# 45)

print("Номер 45", "\n")

month = int (input ("Month is: "))

match month:
    case 1 | 2 | 12: print ("Winter")
    case 3 | 4 | 5: print ("Spring")
    case 6 | 7 | 8: print ("Summer")
    case 9 | 10 | 11: print ("Autumn")
    case _: print ("Error:)")