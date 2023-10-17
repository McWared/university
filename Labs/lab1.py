import math


def _info_about_me():
    """
    info about author
    """
    print("The author of this programm is Andrew Pozhylenkov Group K-10 Variant 20.")
    print("This programm calculates the value of the expression by given x.")

def f(x):
    """
    f(x) function calculates the expression
    """
    result = math.cos(22/55) - 2 * math.pi + \
    54 * math.e * 13 / ((x - 4) * (x + 10)) - \
    11 * math.cos(x + 9) + 13 / (x - 5)

    return result

def _domain(x):
    """
    _domain(x) function checks the domain of the expression
    """
    return x!=4 and x!=-10 and x!=5

def main():
    """
    main() function gathers all auxiliary functions together and does exception checking
    """
    
    _info_about_me()

    try:
        x = float(input("Enter x (!= 4, -10, 5): "))
        print ("***** do calculations ...", end=" ")

        if _domain(x):
            result = f"{f(x):.8f}"
        else:
            result = "undefined"

        print ("done")
        print (f"for x = {x:.6f}")
        print (f"result =", result)

    except KeyboardInterrupt:
        print ("you aborted the programm")
    except Exception:
        print ("wrong input")

main()