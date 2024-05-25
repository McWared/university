import numpy as np
"""Importing numpy as np"""


def _info_about_me():
    """Info about author"""

    print("The author of this programm is Andrew Pozhylenkov Group K-10 Variant 20.")
    print("The program prints the sequence of matrix elements in a spiral along the right quarter-triangle of the matrix\
along the right quarter-triangle of the matrix in a spiral from the upper right corner of the matrix in a clockwise")


def _input_n() -> int:
    """
    User input his value of n.

    Returns:
    --------
    int:
        The size of the matrix
    """
    user_n = int(input('Enter your n (n > 0, n - integer): '))
    return user_n


def _check_n_domain(n: int) -> ValueError:
    """Raises a ValueError if 'n' is does not meet the condition"""
    if n <= 0: raise ValueError('Your n less then 1')


def matrixFill(n: int) -> np.ndarray:
    """
    Filling the matrix with random numbers from the [0.25, 0.75) range.
    
    Arguments:
    ----------
    n: int
        The size of the matrix

    Returns:
    ---------
    np.ndarray:
        The matrix (n x n)
    """
    matrix = np.random.uniform(0.25, 0.75, size = (n, n))
    return matrix


def _isEven(n: int) -> bool:
    """
    Determines whether the matrix is even or odd.

    Arguments:
    ----------
    n: int
        The size of the matrix

    Returns:
    -----------
    bool:
        Even - True, Odd - False
    """
    if (n % 2) == 0:
        return True
    return False


def traversal(matrix: np.ndarray):
    """
    This function prints needed elements by the given order in the given matrix.

    Arguments:
    -----------
    matrix: np.ndarray
        The given squared matrix
    """

    def moveDown(row: int, column: int, number_of_elements: int) -> int:
        """
        Additional function that prints elements vertically down.

        Arguments:
        ----------
        row: int
            The row coordinate of the point, where function starts printing
        column: int
            The column coordinate of the point, where function starts printing
        number_of_elements: int
            The number of elements that this function print per execution

        Returns:
        ----------
        row: int
            The row coordinate of the point, where function starts printing (for the NEXT itteration)
        column: int
            The column coordinate of the point, where function starts printing (for the NEXT itteration)
        number_of_elements: int
            The number of elements that this function print per execution (for the NEXT itteration)
        """
        row_copy = row

        for _ in range(number_of_elements):
            print(f'{matrix[row_copy, column]:.1f}', end = ' ')
            row_copy += 1
        row += 2
        column -= 1
        number_of_elements -= 4

        return row, column, number_of_elements
    

    def moveLeft(row: int, column: int , number_of_elements: int) -> int:
        """
        Additional function that prints elements diagonally up-left.

        Arguments:
        ----------
        row: int
            The row coordinate of the point, where function starts printing
        column: int
            The column coordinate of the point, where function starts printing
        number_of_elements: int
            The number of elements that this function print per execution

        Returns:
        ----------
        row: int
            The row coordinate of the point, where function starts printing (for the NEXT itteration)
        column: int
            The column coordinate of the point, where function starts printing (for the NEXT itteration)
        number_of_elements: int
            The number of elements that this function print per execution (for the NEXT itteration)
        """
        row_copy = row
        column_copy = column

        for _ in range(number_of_elements):
            print(f'{matrix[row_copy, column_copy]:.1f}', end = ' ')
            row_copy -= 1
            column_copy -= 1

        row -= 2
        column -= 1
        number_of_elements -= 2

        return row, column, number_of_elements
    

    def moveRight(row: int, column: int, number_of_elements: int) -> int:
        """
        Additional function that prints elements diagonally up-right.

        Arguments:
        ----------
        row: int
            The row coordinate of the point, where function starts printing
        column: int
            The column coordinate of the point, where function starts printing
        number_of_elements: int
            The number of elements that this function prints per execution

        Returns:
        ----------
        row: int
            The row coordinate of the point, where function starts printing (for the NEXT itteration)
        column: int
            The column coordinate of the point, where function starts printing (for the NEXT itteration)
        number_of_elements: int
            The number of elements that this function print per execution (for the NEXT itteration)
        """
        row_copy = row
        column_copy = column

        for _ in range(number_of_elements):
            print(f'{matrix[row_copy, column_copy]:.1f}', end = ' ')
            row_copy -= 1
            column_copy += 1

        column += 1
        number_of_elements -= 2
        
        return row, column, number_of_elements
    

    n = len(matrix)
    whole_half_n = n // 2

    # start_... variables used for the very first function calls
    start_row_down = 0
    start_column_down = n - 1
    start_number_of_elements_down = n

    start_row_left = n - 2
    start_column_left = n - 2

    if _isEven(n):
        start_row_right = (whole_half_n) - 1
        start_column_right = whole_half_n
        start_number_of_elements_right = (whole_half_n) - 1

        start_number_of_elements_left = (whole_half_n) - 1
    else:
        start_row_right = (whole_half_n) - 1
        start_column_right = (whole_half_n) + 1
        start_number_of_elements_right = (whole_half_n) - 1

        start_number_of_elements_left = whole_half_n

    #This assignment of 3 variables is the trick that i used, after first execution functions runs from this variables in the loop
    row_down, column_down, number_of_elements_down = moveDown(start_row_down, start_column_down, start_number_of_elements_down)
    row_left, column_left, number_of_elements_left = moveLeft(start_row_left, start_column_left, start_number_of_elements_left)
    row_right, column_right, number_of_elements_right = moveRight(start_row_right, start_column_right, start_number_of_elements_right)

    #Flag variable created for helping ending the loop, when 'number_of_elements' of one of the functions is less then 1
    flag = True

    while flag:

        if number_of_elements_down > 0:
            row_down, column_down, number_of_elements_down = moveDown(row_down, column_down, number_of_elements_down)
        else:
            flag = False

        if number_of_elements_left > 0 and flag == True:
            row_left, column_left, number_of_elements_left = moveLeft(row_left, column_left, number_of_elements_left)
        else:
            flag = False

        if number_of_elements_right > 0 and flag == True:
            row_right, column_right, number_of_elements_right = moveRight(row_right, column_right, number_of_elements_right)
        else:
            flag = False


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
