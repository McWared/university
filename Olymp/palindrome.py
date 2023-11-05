n = str(input())
# S не має містити паліндромів завдовжки 2 і більше
def f(n):
    letters = {}
    for symbol in n:
        if symbol in letters:
            letters[symbol] = letters[symbol] + 1
        else:
            letters[symbol] = 1
    if len(letters) == 1:
        return("NO")
    if len(letters) == 3:
        return("YES")
    if (len(n)%2) == 0:
        flag = 1
        for value in letters.values():
            if value % 2 == 1:
                flag = 0
        if flag == 0:
            return("YES")
        else:
            return("NO")
    if (len(n)%2) == 1:
        return("YES")

print(f(n))