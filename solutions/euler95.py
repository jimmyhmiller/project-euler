#!/usr/bin/env python
from util import proper_divisors,memoize,is_prime
from math import sqrt


def list_of_composites(n):
    n_factors = [0]*n 
    for i in xrange(2,int(sqrt(len(n_factors))+1)): 
        if n_factors[i] == 0: 
            for j in xrange(i*2,n,i):
                n_factors[j] +=1 
    primes = [1] + [i for i in range(len(n_factors)) if n_factors[i] > 0]
    return primes


@memoize
def sum_divisors(x):
    return sum(proper_divisors(x))


def chain(x):
    original = x
    i = 1
    smallest = 1000000
    prev = set()
    while 1:
        prev.add(x)
        x = sum_divisors(x)
        if x < smallest:
            smallest = x
        if x == original:
            return i, smallest
        elif x > 1000000 or x in prev:
            return 0, 1000000
        else:
            i += 1


def main():
    print max(chain(i) for i in list_of_composites(100000))
 

if __name__ == '__main__':
    main()

