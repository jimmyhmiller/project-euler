#!/usr/bin/env python
from util import list_of_primes


primes = list_of_primes(1000)
quad = lambda n,a,b: n**2 + a*n + b


def main():
    total = (0,0)
    for a in range(-1000,1000):
        for b in primes:
            n = 1
            while quad(n,a,b) in primes:
                n+=1
            if n > total[0]:
                total = (n,a*b)
    print total[1]


if __name__ == '__main__':
    main()