import math
"""Написати функцію, яка утворює новий список і заповнює його послідовними біномними
коефіцієнтами C௡
௞
(k=0,1,..,n)."""

def pract(n, k):

    res = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return res

def final(n):

    mylist = []
    k = 0
    while k <= n:
        mylist.append(int(pract(n, k)))
        k += 1
    return(mylist)
print(final(10))

def pract2(n, k):

    calc = math.comb(n, k)
    return calc

def final2(n):

    mylist = []
    k = 0
    while k <= n:
        mylist.append(pract2(n, k))
        k += 1
    return(mylist)
print(final2(10))