import numpy as np
"""Importing numpy as np"""


def _info_about_me():
    """Info about author"""

    print("The author of this programm is Andrew Pozhylenkov Group K-10 Variant 20.")
    print("The program prints the sequence of matrix elements in a spiral along the right quarter-triangle of the matrix\
along the right quarter-triangle of the matrix in a spiral from the upper right corner of the matrix in a clockwise")


def _input_n() -> int:
    """User input his value of n."""
    
    user_n = int(input('Enter your n (n > 0, n - integer): '))
    return user_n


def _check_n_domain(n: int) -> ValueError:
    """Raises a ValueError if 'n' is does not meet the condition"""

    if n <= 0: raise ValueError('Your n less then 1')


def matrixFill(n: int) -> np.ndarray:
    """Filling the matrix with random numbers from the [0.25, 0.75) range."""

    matrix = np.random.uniform(0.25, 0.75, size = (n, n))
    return matrix


def _isEven(n: int) -> bool:
    """Determines whether the matrix is even or odd."""

    if (n % 2) == 0:
        return True
    return False


def traversal(matrix: np.ndarray):
    """This function prints needed elements by the given order in the given matrix."""
    
    n = len(matrix)
    whole_half_n = n // 2

    # start_... variables used for the very first function calls
    row_down = 0
    column_down = n - 1
    number_of_elements_down = n

    row_left = n - 2
    column_left = n - 2

    if _isEven(n):
        row_right = (whole_half_n) - 1
        column_right = whole_half_n
        number_of_elements_right = (whole_half_n) - 1

        number_of_elements_left = (whole_half_n) - 1
    else:
        row_right = (whole_half_n) - 1
        column_right = (whole_half_n) + 1
        number_of_elements_right = (whole_half_n) - 1

        number_of_elements_left = whole_half_n

    # if matrix is 1x1
    if n == 1:
        print(f'{matrix[0, 0]:.1f}', end = ' ')

    while number_of_elements_down >= 0 and number_of_elements_left >= 0 and number_of_elements_right >= 0:

        # moveDown
        row_down_copy = row_down

        for _ in range(number_of_elements_down):
            print(f'{matrix[row_down_copy, column_down]:.1f}', end = ' ')
            row_down_copy += 1

        row_down += 2
        column_down -= 1
        number_of_elements_down -= 4

        # moveLeft
        row_left_copy = row_left
        column_left_copy = column_left

        for _ in range(number_of_elements_left):
            print(f'{matrix[row_left_copy, column_left_copy]:.1f}', end = ' ')
            row_left_copy -= 1
            column_left_copy -= 1

        row_left -= 2
        column_left -= 1
        number_of_elements_left -= 2

        # moveRigth
        row_right_copy = row_right
        column_right_copy = column_right

        for _ in range(number_of_elements_right):
            print(f'{matrix[row_right_copy, column_right_copy]:.1f}', end = ' ')
            row_right_copy -= 1
            column_right_copy += 1

        column_right += 1
        number_of_elements_right -= 2


def main():
    """Runs all functions together in the right order and handles the errors."""
    try:
        _info_about_me()

        n = _input_n()
        _check_n_domain(n)

        matrix = matrixFill(n)
        print(matrix)
        
        print('TRAVERSAL')
        traversal(matrix) 
    
    except (ValueError, TypeError, IndexError) as e:
        print('***** error')
        print(f'The problem is: {e}')
    except EOFError as e:
        print("\n***** error")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('\nprogram aborted')
    except (RuntimeError, MemoryError) as e:
        print("***** error")
        print(f'There is problem: {e}')
    except BaseException as e:
        print("***** error")
        print(f'\nThere are a global problem here: {e}')
