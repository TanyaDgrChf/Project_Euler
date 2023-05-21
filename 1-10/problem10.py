from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

x = 1
primes = []

while x <= 2000000:
    x += 1
    if is_prime(x):
        primes.append(x)

print(sum(primes))