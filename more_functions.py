
# write a function that calculates fibonacci

def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# write a function that calculates the factorial of a number

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# write a function that calculates the sum of a list of numbers

def sum_of_list(numbers: list):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_of_list(numbers[1:])