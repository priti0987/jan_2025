from functools import reduce

myList = [1,6,3,3,2]

print(reduce(lambda a,b:a+b,myList))