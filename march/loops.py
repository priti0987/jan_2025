#print 1 2 3 4 5
# for i in range(1,6):
#     print(i,end=" ")
#print square
# for i in range(1,6):
#     print(i**2, end =" ")
#print even numbers from 1 to 10
# for i in range(1,11):
#     if i%2==0:
#         print(i,end=" ")
#calculate sum of numbes from 1 to 10
# sum = 0
# for i in range(1,11):
#     sum +=i
#     # sum = sum+i
# print(sum)
#reverse a word : input => python, output => nohtyp
inputWord = input("Enter word : ")
outputWord = ""
for i in range(len(inputWord)):
    outputWord = inputWord[i]+outputWord

print(outputWord)