#
# numb = 1
# factorial = 1
# if numb<0:
#     print(" no factorial..")
# elif numb == 0:
#     print("factorial = 1")
# else:
#     for i in range(1,numb + 1):
#         # print(i)
#         factorial = factorial*i
#     print(factorial)
#     # print(factorial)


#using recursing method
# 5! = 5*4*3*2*1

def fact(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num*fact(num-1)


print(fact(5))