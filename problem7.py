from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
primeFound = False
x = 1
primes = []
while not primeFound:
    x += 1
    if is_prime(x):
        primes.append(x)
    if len(primes) == 10001:
        primeFound = True
print(primes[10000])
