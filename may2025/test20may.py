myString = "My name is priti"
newString = ""
newString = myString[::-1]
print(newString)
newString=newString.replace(" ","")
newString= list(newString)

print(newString)
for i in range(len(myString)):
    if myString[i]==" ":
        newString.insert(i, " ")
    print(i)
    newString = "".join(newString[i])


#print(spaceindexList)
print(newString)
