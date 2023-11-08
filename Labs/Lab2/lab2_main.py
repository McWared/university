A = 0
B = 1

def _info_about_me():
    """
    Info about author
    """
    print("The author of this programm is Andrew Pozhylenkov Group K-10 Variant 20.")
    print("This programm calculates the value of the series by given x and eps (accuracy).")

def s(x: float, eps: float) -> float:
    """
    Calculates the value of an expression using a series approximation with a given accuracy.

    Args:
        x (float): The value for which the expression is calculated.
        eps (float): The desired accuracy of the calculation.
    """
    a = 1
    s = a
    n = 1
    n = n * n
    while -eps <= a >= eps:
        a *= -x / n
        s += a
        n += 1
    return s

def _domain_x(x: float) -> bool:
    """
    Check if the input value `x` is within the specified domain.

    Args:
        x (float): The input value to be checked against the domain.
    """
    if A < x > B:
        raise ValueError("x is out of domain")

def _domain_eps(eps: float) -> bool:
    """
    Check if the input `eps` is less than or equal to zero.

    Args:
        eps (float): The value of eps to be checked.
    """
    if eps <= 0:
        raise ValueError("eps is less than 0")


def main() -> float:
    """
    Gathers all auxiliary functions together and does exception checking
    """

    _info_about_me()

    try:
        x = float(input(f"Enter x from [{A}, {B}]: "))
        _domain_x(x)
        eps = float(input("Enter eps > 0: "))
        _domain_eps(eps)

        print ("***** do calculations ...", end=" ")
        result = s(x, eps)

        print("done")
        print (f"for x = {x:.8f}")
        print (f"for eps = {eps:.7f}")
        print (f"result = {result:.11f}")

    except (ValueError, EOFError) as e_mes:
        print("***** error")
        print("The reason is:", e_mes)

try:
    main()
except KeyboardInterrupt as e_mes:
    print("\nprogram aborted")