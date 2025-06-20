listl = [2, 5, 6, 8, 1, 8, 9, 11]
#listl.sort()
max = listl[0]
print(max)
for i in range(len(listl)):
    if max <listl[i]:
        max=listl[i]

print(max)


