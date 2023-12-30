import threading

def factorial_of_a_number(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def calculate_factorial(n):
    result = factorial_of_a_number(n)
    print(f"Factorial of {n} is {result} ")

n =int(input())

thread1 = threading.Thread(target=calculate_factorial, args=(n,))

thread1.start()

thread1.join()
