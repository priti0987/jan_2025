# python challenge remove repetition​ of letter from string or give me unique letter only

myString = "aabbbhhheerrddvcgdfgdg"
myList=[]
for i in myString:
    myList.append(i)
myset = set(myList)
sorted(myset)
print("".join(sorted(myset)))