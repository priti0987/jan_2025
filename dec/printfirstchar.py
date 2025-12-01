inputString = "pwelcome rto ipython tclass"

outputString = ""
mystring =inputString.split()
for i in mystring:
    outputString = outputString + i[0]

print(outputString)