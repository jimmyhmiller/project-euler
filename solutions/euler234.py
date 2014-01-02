from util import list_of_primes, memoize
from math import sqrt

primes = list_of_primes(1000000)

     
@memoize
def lups(n):
    sqrt_n = sqrt(n)
    if sqrt_n % 1 == 0:
        return (sqrt_n, sqrt_n)
    i = 0
    while primes[i] <= sqrt_n:
        i += 1
    return primes[i-1], primes[i]


def main():    
    print sum(i for i in range(4,1000000) if (i % lups(i)[0] == 0) != (i % lups(i)[1] == 0))

if __name__ == '__main__':
    main()