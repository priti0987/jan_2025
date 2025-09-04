# # inputString = "test12pop90java989pyt"
# # #outputString = "tset21pop90avaj989typ"
# # myDictionary ={}
# # for i in range(len(inputString)):
# #     myDictionary[i]=inputString[i]
# #
# # # print(myDictionary)
# # myString = ""
# # for i in inputString:
# #     if i.isnumeric():
# #         myString=myString+" "
# #     else:
# #         myString=myString+i
# # # print(myString)
# # myspilstring=myString.split("  ")
# # outstring1=""
# # for i in myString:
# #     if i != " ":
# #         outstring1 = outstring1+i[::-1]
# #     else:
# #         outstring1.join(" ")
# # print(outstring1)
#
#
#
# s = "Welcome234To567Java89Programming0@#!!"
# sAlpha = []
# sAlpha1=""
# sNum = []
# sNum1=""
# sSpe=[]
# sSpe1=""
# for i in s:
#
#     if i.isalpha():
#         sAlpha1 = sAlpha1+i
#     elif i.isdigit():
#         sNum1= sNum1 +i
#     else:
#         sSpe1 = sSpe1+i
#
# print(sAlpha1)
# print(sNum1)
# print(sSpe1)
# # print(sAlpha1.join(sAlpha))
# # print(sNum1.join(sNum))
# # print(sSpe1.join(sSpe))
subString= ""
sub1=""
indexNum = []
num=[]
inputString = "test12pop90java989pyt"
for i in range(len(inputString)):
    if inputString[i].isalpha():
        subString = subString +inputString[i]

    elif inputString[i].isdigit():
        # print(i)
        indexNum.append(i)
        num.append(inputString[i])
    sub1 = sub1+(subString[::-1])

print(sub1)
print(indexNum)
print(num)