def _domain(n):
    if n<0:
        raise ValueError("n is less then 0.")

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def main():

    try:
        n = int(input("Enter n >= 0: "))
        _domain(n)
        print(factorial(n))
    except Exception as error:
        print ("There is smth wrong", error)
        print (type(error).__name__)

main()