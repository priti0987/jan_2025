myList = ['apple','mango','banana','mango','chikoo','banana','mango']

uniqueValue =set()
duplicate = []

for i in myList:
    if i in uniqueValue and i not in duplicate:
        duplicate.append(i)
    uniqueValue.add(i)

print(duplicate)
print(list(uniqueValue))