myList = [1,1,2,5,6,3,5,15,6]

unique = []
duplicate = []
for i in myList:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
print(unique)
print(list(set(myList)))
print(duplicate)

