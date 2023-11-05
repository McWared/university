n = int(input())
def main(n):
    """
    Calculates the factorial index of a number until it matches 'n'.

    Args:
        n (int): The number for which the factorial index needs to be found.

    Returns:
        int: The index at which the factorial of a number matches 'n'.
    """
    index = 0
    result = 1
    while True:
        index += 1
        result *= index
        if result == n:
            return index
print(main(n))