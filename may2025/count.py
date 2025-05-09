myString = "My name is priti "
count = 1
for i in myString:
    if i == " ":
        count = count +1

myString1 = myString.split(" ")
for i in myString1:
    if i.__contains__("p"):
        print(i)
print(count)