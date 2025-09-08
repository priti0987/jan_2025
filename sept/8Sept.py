#check number is prime or not


myNumber = 5
coun=0
if myNumber >1:
    for i in range(1,myNumber):
        if myNumber%i==0:
            coun+=1

if coun==1:
    print("Number is prime")
else:
    print("Number is not prime")
