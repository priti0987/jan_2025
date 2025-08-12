# https://www.youtube.com/watch?v=iCwkuJOxvRI&list=PL3JNM3ENFH-5r3mRfuIbXLRCvtNK0FhmU
# input from user :: rent , food, electric , charge perunit, person living in flat

rent =int(input("Enter rent = "))
food =int(input("Enter food = "))
electricCharges =int(input("Enter electricCharges = "))
chargePerUnit =int(input("Enter chargePerUnit = "))
person = int(input("Enter number of persons = "))

totalElectricBill = electricCharges*chargePerUnit

totalrentforonePerson = (totalElectricBill+food+rent)//person

print("Each person have to pay = ",totalrentforonePerson)