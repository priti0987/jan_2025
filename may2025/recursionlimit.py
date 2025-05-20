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
#
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

#print ur name 10times dnt user loop and manually

# n=1
# def printmyname(name):
#     global n
#     if n<=10:
#         print(name)
#         n+=1
#         printmyname(name)
#
# printmyname("priti")


n=10
def nameprint(name):
    global n
    while n>0:
        print(name)
        n-=1
        nameprint(name)
nameprint("pratap")