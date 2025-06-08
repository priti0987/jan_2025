s1="danger"
s2="gardeun"

def isvalidanagram(s1,s2):
    answer=True
    for i in s1:
        if i in s2:
            print("true= ",i)
        else:
            answer=False


    for i in s2:
        if i in s1:
            print("true= ",i)
        else:
            answer = False
    return answer

print(isvalidanagram(s1,s2))