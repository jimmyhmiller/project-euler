#!/usr/bin/env python
from util import is_prime


def diagonal(n):
    return n**2-(n-1), n**2 - 2*(n - 1), n**2 - 3*(n - 1)


def main():
    prime_perc = 100
    total = 1
    num_prime = 0
    i = 1
    while prime_perc >= .10:
        i+=2
        total += 4
        for d in diagonal(i):
            num_prime += is_prime(d)
        prime_perc = float(num_prime)/total

    print i,prime_perc 


if __name__ == '__main__':
    main()