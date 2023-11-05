import math

n = int(input())

def main(n):
    index = 0
    fact = math.factorial(index)
    while fact != n:
        index += 1
        fact = math.factorial(index)
    return index
print(main(n))