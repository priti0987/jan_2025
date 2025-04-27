#function calling it self is called recursion


#example factorial

def factorial(number):
    if number == 1:
        return number
    else:
        return number*factorial(number-1)


print("facccc=",factorial(3))


def add_one(num):
    if num >=9:
        return num + 1
    total = num +1
    print(total)
    return add_one(total)

add_one(10)