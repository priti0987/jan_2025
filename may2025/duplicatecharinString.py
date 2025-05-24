from collections import Counter

myString= "pratap"

#
# mydictionary = {}
#
# mylist = list(myString)
# # for i in myString:
# #     if
# # print(mylist[0])
# for i in range(len(myString)):
#     # print(myString[i])
#     # print(myString.count(mylist[i]))
#     if myString.count(mylist[i]) ==2:
#         print(myString[i])
#     mydictionary[myString[i]] = myString.count(mylist[i])
#
# # print(mydictionary)


def dupp(stringg):
    c=Counter(stringg)
    print(c)
    for w,c1 in c.items():
        if c1>1:
            print(w)
dupp("pratap")