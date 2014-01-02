#!/usr/bin/env python
from util import list_of_primes


def truncate_left(x):
    for i in range(1,len(x)):
        yield  x[i:] 


def truncate_right(x):
    for i in range(len(x)-1,0,-1):
        yield x[:i] 


def main():  
    answers = []
    primes = list_of_primes(1000000)
    primes = [str(p) for p in primes]
    master = set(primes)
    left = lambda x: all(i in master for i in truncate_left(x))
    right = lambda x: all(i in master for i in truncate_right(x))
    primes = [p for p in primes if not "0" in p and not "4" \
        in p and not "6" in p and not "8" in p and not "5" in p]
    primes = [p for p in primes if p[0] != "9" or p[-1] != "9"]
    primes = [p for p in primes if left(p) and right(p)]
    primes = [p for p in primes if len(p) > 1]
    primes = [int(p) for p in primes]
    print sum(primes)


if __name__ == '__main__':
    main()