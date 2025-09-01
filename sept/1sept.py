#Find Factors of a Number

# def factors(numb):
#     for i in range(1,numb+1):
#         if numb % i ==0:
#             print(i)
#
#
# factors(6)

#Monotonic or not?
def monotonic(list):
    for i in range(list-1):
        if all(list[i]>list[i+1]):
            return True
        elif all(list[i] < list[i + 1]):
            return False

list1=[1,5,6,2,3,7]
list2=[4,5,6,7,8]

print(monotonic(list2))
print(monotonic(list1))