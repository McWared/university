lst = [1,23,4,1,'privet',True,0,-192]
intlst = [0,0,0,0,1,2,3,4,5,6,7,8,9,1]

# Файл 16, номер 4
def create () -> list:

    try:
        mylist = []
        elem = int(input())

        while True:
            mylist.append(elem)
            elem = int(input())
    except (ValueError, EOFError):
        return mylist

# Файл 16, номер 8

def add (lst: list, el) -> int:
    """
    Написати функцію, що додає в список елемент, якщо його там нема. В усіх випадках повертається
    індекс елемента.
    """
    if el not in lst:
        lst.append(el)
    
    print(lst.index(el))

# Файл 16, номер 10

def even_out (lst: list) -> list:
    """
    Написати функцію, що виводить усі парні елементи списку цілих.
    """
    print([elem for elem in lst if elem % 2 == 0])

# Файл 16, номер 13

def removezero (lst: list) -> list:
    """
    Написати функцію, що з списку цілих вилучає усі нульові елементи.
    """
    print([x for x in lst if x != 0])