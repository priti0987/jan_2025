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

pattern2(6)