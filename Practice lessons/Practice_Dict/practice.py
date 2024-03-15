"""Написати функцію, що за послідовністю цілих, утворює словник, що зберігає множину її елементів
як множину з повтореннями."""
n = [1,2,1,3,2]

def solution(n: list):
    alphabet = {}
    for element in set(n):
        alphabet[element] = n.count(element)
    return alphabet

print(solution(n))