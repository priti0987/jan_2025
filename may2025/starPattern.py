def pattern1(n):
    for i in range(n):
        for j in range(i):
            print("*",end="")
        print("")

def pattern2(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print("")


def pattern3(n):
    for i in range((2*n)):
        if i>n:
            c=(2*n)-i
        else:
            c=i
        # for ii in range(n-c):
        #     print(" ",end="")
        for j in range(c):
            print("*",end="")
        print("")

pattern3(7)