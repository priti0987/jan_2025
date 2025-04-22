#Q: "radar" palendrome :: write code


inputString = "priti"

if inputString == inputString[::-1]:
    print(f"Given String {inputString} is palendrome")
else:
    print(f"Given String {inputString} is not a palendrome")

#print horizontally

listl = [1, 3, 6, 7]
for number in listl:
    print(number, end= " ")
# Output:
# 13 6 7