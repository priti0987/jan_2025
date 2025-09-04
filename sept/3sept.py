# # #outputString = "tset21pop90avaj989typ"
inputString = "test12pop90java989pyt"
input = "swiss" #index of nonconsistence char
# output = W1

def nonrepeatingchar(s):
    charCount ={}
    for i in s:
        if i in charCount:
            charCount[i]+=1
        else:
            charCount[i]=1

    for i in range(len(s)):
        if charCount[s[i]]==1:
            return i
    return -1

print(nonrepeatingchar('swiss'))