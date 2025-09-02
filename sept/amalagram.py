string1 = "listen"
string2 = "silent"
# count = 0
# if len(string2)== len(string1):
#     for i in string1:
#         if i in string2:
#             count =count+1
#
# if count == len(string1):
#     print("Given string is anagram")

def isanagram(str1,str2):
    return sorted(str1.lower())==sorted(str2.lower())

if isanagram(string1,string2):
    print("Anagram")
else:
    print("Not anagram")