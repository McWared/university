def sir (m:int) -> int:

    f2, f1 = 0, 1

    while f1 < m:
        f2, f1 = f1, f1 + f2
    print(f1)

sir(9)