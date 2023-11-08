# Файл 16, номер 18

a = [1,2,3,-1,-2,-3]

def test(a: list):
    min = None
    for num in a:
        if num > 0 and num < min:
            if num < min:
                min = num
    return min

print(test(a))