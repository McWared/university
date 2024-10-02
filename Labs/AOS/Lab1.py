import time

def add_int_time(COUNT):
    num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5

    start = time.time()
    for i in range(COUNT):
        num1 + i
        num2 + i
        num3 + i
        num4 + i
        num5 + i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def subtract_int_time(COUNT):
    num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5

    start = time.time()
    for i in range(COUNT):
        num1 - i
        num2 - i
        num3 - i
        num4 - i
        num5 - i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def multiply_int_time(COUNT):
    num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5

    start = time.time()
    for i in range(COUNT):
        num1 * i
        num2 * i
        num3 * i
        num4 * i
        num5 * i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def divide_int_time(COUNT):
    num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5

    start = time.time()
    for i in range(1, COUNT + 1):
        num1 / i
        num2 / i
        num3 / i
        num4 / i
        num5 / i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def add_float_time(COUNT):
    num1, num2, num3, num4, num5 = 1.0, 2.0, 3.0, 4.0, 5.0

    start = time.time()
    for i in range(COUNT):
        num1 + i
        num2 + i
        num3 + i
        num4 + i
        num5 + i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def subtract_float_time(COUNT):
    num1, num2, num3, num4, num5 = 1.0, 2.0, 3.0, 4.0, 5.0

    start = time.time()
    for i in range(COUNT):
        num1 - i
        num2 - i
        num3 - i
        num4 - i
        num5 - i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def multiply_float_time(COUNT):
    num1, num2, num3, num4, num5 = 1.0, 2.0, 3.0, 4.0, 5.0

    start = time.time()
    for i in range(COUNT):
        num1 * i
        num2 * i
        num3 * i
        num4 * i
        num5 * i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def divide_float_time(COUNT):
    num1, num2, num3, num4, num5 = 1.0, 2.0, 3.0, 4.0, 5.0

    start = time.time()
    for i in range(1, COUNT + 1):
        num1 / i
        num2 / i
        num3 / i
        num4 / i
        num5 / i
    finish = time.time()

    return (5 * COUNT / (finish - start))

def add_string_time(COUNT):
    str1 = "hello"
    str_list = [str(x) for x in range(COUNT)]

    start = time.time()
    for string in str_list:
        str1 + string
        str1 + string
        str1 + string
        str1 + string
        str1 + string
    finish = time.time()

    return (5 * COUNT / (finish - start))

def main():
    COUNT = 30000000

    functions_times = [
        add_int_time(COUNT), subtract_int_time(COUNT), multiply_int_time(COUNT),
        divide_int_time(COUNT), add_float_time(COUNT), subtract_float_time(COUNT),
        multiply_float_time(COUNT), divide_float_time(COUNT), add_string_time(COUNT)
        ]
    
    operations = ["+", "-", "*", "/", "+", "-", "*", "/", "+"]
    types = ["int", "int", "int", "int", "float", "float", "float", "float", "string"]

    max_of_functions_times = max(functions_times)

    for i in range(len(functions_times)):
        value = functions_times[i]
        percent = round((value / max_of_functions_times) * 100)

        print(f'{operations[i]:<5} {types[i]:<10} {value:<25} {"∆" * int(percent):<101} {percent}%')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'There is a problem: {e}')