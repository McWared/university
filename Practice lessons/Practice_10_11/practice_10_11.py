# Файл 9 (Задачі та вправи)

# Номер 1 (б)

a = 1
b = 1

''' Ці змінні по факту нічого не роблять, оскільки "а" та "b" визначені ниже '''

def f(a):
    a += 1
    return a

def g(x):
    x = 2 + b
    return a

a = 3
b = 4

''' Оскільки виклик функцій після означення цих змінних - будуть використані саме вони (a = 3, b = 4) '''

print(f(a), g(b), a, b)

# Номер 1 (в)

a = 1
b = 1

def f(b):
    global a
    a += 1 + b
    return a

''' 
Тут при працюємо напряму зі змінною "а" (тому що global), тобто ії значення буде змінюватися
Після виклику цієї функції змінна а буде дорівнювати 7 (3 += 1 + 3)
'''

def g(x):
    a = 2
    x = a + b
    return x

a = 3
b = 4

print(f(a), g(b), a, b)