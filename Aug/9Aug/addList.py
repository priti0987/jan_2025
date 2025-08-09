myList1 = [1,2,5,6]
myList2 = [4,1,2,1]
outList = []

outList = myList2+myList1
print("It will add number of items in list")
print(outList)
outList = []

print("index wise add in list")
for i in range(len(myList1)):
    outList.append(myList1[i]+myList2[i])

print(outList)