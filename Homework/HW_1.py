import math

def task_1():

    x = float(input("Enter x: "))
    sin = math.sin(x)
    cos = math.cos(x)

    print(f'For x = {x} sin(x) = {sin}')
    print(f'For x = {x} cos(x) = {cos}')

    if int(cos) == 0:
        print(f"For x = {x} tan(x) = {'error, your value is not in domain (cos(x) == 0)'}")
    else:
        print(f"For x = {x} tan(x) = {math.tan(x)}")

    if int(sin) == 0:
        print(f"For x = {x} cot(x) = {'error, your value is not in domain (sin(x) == 0)'}")
    else:
        print(f"For x = {x} cot(x) = {1 / math.tan(x)}")

    if x >= 1 and x <= -1:
        print(f"For x = {x} asin(x) = {'error, your value is not in [-1;1]'}")
    else:
        print(f"For x = {x} asin(x) = {math.asin(x)}")

    if x >= 1 and x <= -1:
        print(f"For x = {x} acos(x) = {'error, your value is not in [-1;1]'}")
    else:
        print(f"For x = {x} acos(x) = {math.acos(x)}")

    atan = math.atan(x)
    print(f'For x = {x} atan(x) = {atan}')

    if x == 0:
        acot = math.pi/2
    elif x > 0:
        acot = math.atan(1 / x)
    else:
        math.pi + math.atan(1 / x)
    print(f'For x = {x} acot(x) = {acot}')
    
    if x > 0:
        ln = math.log(x, math.e)
        print(f'For x = {x} ln(x) = {ln}')
    else:
        print(f"For x = {x} ln(x) = {'error, your value is not in (0; +inf)'}")

    if x > 0:
        print(f'For x = {x} lg(x) = {math.log10(x)}')
    else:
        print(f"For x = {x} lg(x) = {'error, your value is not in (0; +inf)'}")

def task_2_3(l: list):
    if l:
        el = 0
        while el < len(l) - 1:
            print(l[el],end=',')
            el += 1
        else:
            print(l[-1],end='.\n')
    else:
        print('Your list is empty!')

def task_2_4():
    try:
        out = []
        while True:
            inp = input('Enter your integer: ')
            out.append(int(inp))
    except ValueError:
        print(out)
        print('Your last input cannot convert to int')
    except EOFError:
        print(out)
        print('Program aborted')
        
def task_2_8(elem, lst:list):
    if elem not in lst:
        lst.append(elem)
    return f'Index of your element is: {lst.index(elem)}'

def task_2_19(lst:list):
    """
    Написати функцію, що повертає індекс останнього найбільшого від'ємного елемента списку. Якщо
    від'ємних елементів нема, має повертатись -1.
    """
    maxNeg = min(lst)
    for num in lst:
        if num < 0 and num > maxNeg:
            maxNeg = num
    if maxNeg >=0:
        return -1