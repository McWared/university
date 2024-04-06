import numpy as np

def _info_about_me():
    """
    Info about author
    """
    print("The author of this programm is Andrew Pozhylenkov Group K-10 Variant 20.")
    print("The program prints the numbers in the given order")

def _input_n() -> int:
    """
    User input his n, n - matrix size
    """
    users_n = int(input('Enter your n (n > 0): '))
    return users_n

def _check_n_domain(n: int) -> ValueError:
    """
    Raises a ValueError if 'n' is does not meet the condition
    """
    if n < 1: raise ValueError('your n less then 1')

def matrixFill(n: int):
    """
    Filling the matrix with random numbers from the [0.25, 0.75) range
    """
    matrix = np.empty((n, n))

    for i in range(n):
        for j in range(n):
            randomNumber = np.random.uniform(0.25, 0.75)
            matrix[i, j] = randomNumber
    return matrix

def _isEven(n: int) -> bool:
    """
    Determines whether the matrix is even or odd
    """
    if (n % 2) == 0:
        return True
    return False

def traversal(matrix):
    pass


def main():
    try:
        _info_about_me()

        n = _input_n()
        _check_n_domain(n)

        matrix = matrixFill(n)
        print(matrix)
        
        print('TRAVERSAL')
        traversal(matrix) 
    
    except ValueError as e:
        print('***** error')
        print(f'The problem is: {e}')
    except EOFError as e:
        print("\n***** error")

try:
    main()
except KeyboardInterrupt as e:
    print('\nprogram aborted')
except BaseException as e:
    print(f'\nThere are a global problem here: {e}')
