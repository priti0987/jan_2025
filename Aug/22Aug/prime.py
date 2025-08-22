def isPrime(numb):
    count = 0
    for i in range(1, numb + 1):  # Include numb itself
        if numb % i == 0:
            count += 1

    return count == 2  # True if divisible by only 1 and itself

# Check primes from 1 to 9
for i in range(1, 10):
    if isPrime(i):
        print("It's a prime number:", i)
