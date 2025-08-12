# https://www.youtube.com/watch?v=wjTkqB1DZXw&list=PLKHXue0VSVsRXNgt9s-AXbHoKJwSUI1dO&index=36

myString = "w23e#$%l*&*8989co(*)7434242me"
output = ""
for char in myString:
    if char.isalpha():
        output = output + char

print(output)
output1=""
for n in myString:
    if n.isnumeric():
        output1 = output1 + n

print(output1)
