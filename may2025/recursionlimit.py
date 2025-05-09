# import  sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(100)
# print(sys.getrecursionlimit())

#Direct recurtion
#
# n = int(input("Enter n : "))
#
# def print_naturalNumber(n):
#     print(n)
#     if n==1:
#         return
#     return print_naturalNumber(n-1)
#
# print_naturalNumber(n)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))