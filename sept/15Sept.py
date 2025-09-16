str = "{This is Wissen technology"
#outstring if false coz closing bracket is not there for [

def isbrcketOK(str):
    numbrOfBrk=0
    closingBrkt = 0
    flag = ""
    for i in str:
        if i =='{' :
            numbrOfBrk=numbrOfBrk+1
            if '}' in str:
                    flag="valid string"
                    closingBrkt=closingBrkt+1
        if i=='(':
            numbrOfBrk=numbrOfBrk+1
            if ')' in str:
                flag = "valid string"
                closingBrkt=closingBrkt+1
        if  i=='[':
            numbrOfBrk=numbrOfBrk+1
            if ']' in str:
                flag = "valid string"
                closingBrkt = closingBrkt + 1
            else:
                flag="Invalid String"
    if closingBrkt == numbrOfBrk:
        flag="validd"
    else:
        flag = "Invalidd string"
    return flag
print(isbrcketOK(str))