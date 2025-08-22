def isPrime(numb):
    count = 0
    for i in range(1,numb+1):
        if (numb%i==0):
            count =count+1

    if count==2:
        return True
    else:
        return False


for i in range(1,10):
    if (isPrime(i)):
        print("its a prime number",i)


