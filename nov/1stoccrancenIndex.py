myString = "priti"

mString1 = enumerate(myString)

myDictionary = {}

for i ,ch in mString1:
    if ch not in myDictionary:
        myDictionary[ch] = i


print(myDictionary)