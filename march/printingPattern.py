#test
print("star pattern sums")
#nexted loop
# 1 star pattern ,
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

for i in range(5):
    for i in range(5):
        print("*",end=" ")
    print()

'''Print tringle increamental with left'''

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()


'''Print tringle increamental with upsidedown'''

for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


'''
print
1
12
123
1234
12345 with space 
'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


'''
 print
 5 4 3 2 1
 4 3 2 1
 3 2 1
 2 1
 1'''

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
