#reverse word at odd index
myString = "My name is tiya bhushan fuse"
# outString  ="It irps ie manym"
newString = ""
newString = myString[::-1]
newString=newString.lower()
newString=newString.capitalize()
newString=newString.replace(" ","")
newString= list(newString)
for i in range(len(myString)):
    if myString[i]==" ":
        newString.insert(i, " ")
newString = "".join(newString)
print(newString)
