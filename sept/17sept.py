# #interger in decimal
#
# import decimal
# i=10.2
# iD = decimal.Decimal(i)
# print(type(i))
# print(iD)
# print(type(iD))
#
# #string to decimal
#
# pri = "456"
# print(type(pri))
# newI=decimal.Decimal(pri)
# print(newI)
# print(type(newI))
#
#find duplicates words in a sentence
mysentence = "happy bday to you to pri pri to you to you pri pri"
words = mysentence.split()
print(words)
count = 0
for i in range(0,len(words)):
    count=1
    if words[i]!="0":

        for j in range(i+1,len(words)):
            if words[i]==words[j]:
                count=count+1
                words[j] = "0"

    if count>1:
        print(words[i])