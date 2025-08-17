# single value return 

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number-1)


def sum_of_digits(number):
    if number == 0:
        return 0
    return (number % 10) + sum_of_digits(number // 10)

def fib(number):
    if number == 0 or number == 1:
        return number
    return fib(number-1) + fib(number-2) 

def fib2(number):
    if number < 0:
        return []
    if number == 0:
        return [0]
    if number == 1:
        return [1]
    
    result = fib2(number-1) + fib2(number-2)
    return [result]


def return_chars(string,index):
    if string == "":
        return ""
    if index >= len(string):
        return
    
