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
    if n < 0: raise ValueError('your n less then 1')

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

def traversal(matrix: np.ndarray):
    n = len(matrix)    

    start_row_down = 0
    start_column_down = n - 1
    start_number_of_elements_down = n

    start_row_left = n - 2
    start_column_left = n - 2

    if _isEven(n):
        start_row_right = (n // 2) - 1
        start_column_right = n // 2
        start_number_of_elements_right = (n // 2) - 1

        start_number_of_elements_left = (n // 2) - 1
    else:
        start_row_right = (n // 2) - 1
        start_column_right = (n // 2) + 1
        start_number_of_elements_right = (n // 2) - 1

        start_number_of_elements_left = n // 2


    def moveDown(row, column, number_of_elements):
        row_copy = row

        for i in range(number_of_elements):
            print(f'{matrix[row_copy, column]:.1f}', end = ' ')
            row_copy += 1
        row += 2
        column -= 1
        number_of_elements -= 4

        return row, column, number_of_elements
    

    def moveLeft(row, column, number_of_elements):
        row_copy = row
        column_copy = column

        for i in range(number_of_elements):
            print(f'{matrix[row_copy, column_copy]:.1f}', end = ' ')
            row_copy -= 1
            column_copy -= 1
        row -= 2
        column -= 1
        number_of_elements -= 2

        return row, column, number_of_elements
    

    def moveRight(row, column, number_of_elements):
        row_copy = row
        column_copy = column

        for i in range(number_of_elements):
            print(f'{matrix[row_copy, column_copy]:.1f}', end = ' ')
            row_copy -= 1
            column_copy += 1
        column += 1
        number_of_elements -= 2
        
        return row, column, number_of_elements


    row_down, column_down, number_of_elements_down = moveDown(start_row_down, start_column_down, start_number_of_elements_down)
    row_left, column_left, number_of_elements_left = moveLeft(start_row_left, start_column_left, start_number_of_elements_left)
    row_right, column_right, number_of_elements_right = moveRight(start_row_right, start_column_right, start_number_of_elements_right)

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
