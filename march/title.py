string1 = "hi how are you?"
print(string1)
# print(string1.split(" "))
l = []
for i in string1.split(" "):
    # print(i.capitalize())
    l.append(i.capitalize())
print(" ".join(l))
