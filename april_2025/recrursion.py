#function calling it self is called recursion


#example factorial

def factorial(number):
    if number == 1:
        return number
    else:
        return number*factorial(number-1)


print(factorial(3))