myList = [1,1,2,5,6,3,5,15,6]

unique = []
for i in myList:
    if i not in unique:
        unique.append(i)
print(unique)
print(list(set(myList)))