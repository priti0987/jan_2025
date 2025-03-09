#normal list
#9marchh2025

#print list of numbers which are in range till 10 and divisible by 3

mylist = []
for i in range(10):
    if i %3==0:
        mylist.append(i)
print(mylist)


print([i  for i in range(10) if i%3==0])