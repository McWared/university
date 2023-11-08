A = 0
B = 1

def s(x: float, eps: float) -> float:
    """
    s(x) function calculates the expression with the given accuracy
    """
    a = -x
    s = a
    n = 1
    n = n * n
    while -eps <= a >= eps:
        a *= -x / n
        s += a
        n += 1
    return s