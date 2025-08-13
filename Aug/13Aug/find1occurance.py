# #Finding First occurrence of every char in the string along with indices
#
# myString = "Priti Bhavika Pratap"
#
# myString1 = myString.split(" ")
# print(myString1)
# for i in myString1:
#     print(i)
#     print(i[0])


myString ="presentation"
myDictionary = {}
mystring_enu = enumerate(myString)
for i,char in mystring_enu:
    if char not in myDictionary:
        myDictionary[char]=i
print(myDictionary)
