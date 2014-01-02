#!/usr/bin/env python
from util import factorial,digits, memoize


@memoize
def fact_digits(x):
    return sum(factorial(i) for i in digits(x))
    
def chain(x):
    seq = set()
    seq.add(x)
    while 1:
        x = fact_digits(x)
        if x in seq:
            return len(seq)
        else:
            seq.add(x)
            

def main():
    print sum(1 for i in range(1000000) if chain(i) == 60)
        


if __name__ == '__main__':
    main()