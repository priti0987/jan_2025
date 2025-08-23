#method 1 for loop

myString = "Welcome"
count = 0
# for i in myString:
#     count=count+1
#
# print(count)

#method 2 : while and slicing
# while myString[count :]:
#     count=count+1
# print(count)
#method3 len()

# print(len(myString))

#method 4 :using join and count
randomStr = "we"
print(randomStr.join(myString).count(randomStr)+1)
