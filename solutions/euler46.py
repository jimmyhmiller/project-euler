#!/usr/bin/env python
from util import list_of_primes


twice_squares = [2*i**2 for i in range(1000)]
primes = list_of_primes(100000)
odd_comp = [i for i in range(3,10000,2) if i not in set(primes) ]


def is_equal(o):
    s = 0
    p = 0
    while twice_squares[s] < o:
        while primes[p] < o:
            if twice_squares[s] + primes[p] == o:
                return True
            p+=1
        s += 1
        p = 0
    return False


def main():
    for o in odd_comp:
        if not is_equal(o):
            print o
            exit()
            
if __name__ == '__main__':
    main()