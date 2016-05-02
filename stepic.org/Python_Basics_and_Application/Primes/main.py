import itertools
def isPrime(n):
    d = n - 1
    while d > 1:
        if n % d == 0:
            return False
        d -= 1
    return True
def primes():
    number = 2
    while True:
        if isPrime(number):
            yield number
        number += 1
print(list(itertools.takewhile(lambda x : x <= 31, primes())))