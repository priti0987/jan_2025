namel = {"kelly": 23,"Derick": 14, "John": 7}
name2 = {"Ravi": 45, "Mpho": 67}
#names = namel | name2
names ={**namel,**name2}
print(names)
