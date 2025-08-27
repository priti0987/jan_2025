# #printing horizontally
#
# list1 = [1,3,2,44,5]
# print(list1)
# for i in list1:
#     print(i,end=' ')
#


# #print date
# print()
# print('12','12','1984',sep="/")

#Merging Dictionaries
# myDictionary1 = {"name":"Bhavika","std":"10"}
# myDictionary2 = {"name":"pratap","std":"5"}
# mydictionary = myDictionary1 | myDictionary2
# addDictionry = {**myDictionary1,**myDictionary2}
# print(mydictionary)
# print(addDictionry)


#Calendar with Python
# import calendar
#
# mon = calendar.month(2025,8)
# print(mon)
# isleapYear = calendar.isleap(2024)
# print(isleapYear)

# Get Current Time and Date
#
# from datetime import date
#
# # timeNow = datetime.now()
# timeNow = date.today()
# print(timeNow.strftime('%H:%M:%S'))
# print(timeNow.today())


# Sort a List in Descending Order

# myList = [1,5,88,45,49,2,65,2]
# print(set(myList))
# myList.sort()
# print(myList)
# (myList.sort(reverse=True))
# print(myList)
#swapping numbers
# a= 5
# b=6
# print("Before swapping a is ",a)
# print("Before swapping b is ",b)
# a,b =b,a
#********************
# temp = a
# a=b
# b= temp
#*********************
# a=a+b
# b=a-b
# a=a-b
#*********************
# a=a*b
# b=a//b
# a=a//b
#*********************
# a^=b
# b^=a
# a^=b
# print("After swapping a is ",a)
# print("After swapping b is ",b)

#Counting Item Occurrences
from collections import Counter

# myList = ['John','Kelly','Peter','Peter','Moses']
# # print(Counter(myList).get('Peter'))
# count1 = 0
#
# for i in myList:
#     if i == 'Peter':
#         count1 = count1+1
# print(count1)


# Flatten a Nested List
#
# myList = [[1,3,2],[2,3,4]]
# newList =[]
# for i in myList:
#     for j in i:
#         newList.append(j)
#
# print(newList)
#
# newList1=[i for j in myList for i in j]
# print(newList1)

# Index of the Biggest Number

myList = [12,45,67,89,13,67,34]
mmax= max(myList)
print(mmax)
print(myList.index(mmax))