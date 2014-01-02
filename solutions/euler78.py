#!/usr/bin/env python
from util import memoize


total = 3
denominations = range(1,4)


def count_comb(left,i=0):
    if left == 0 or (i+1) == len(denominations):
        return 1
    return sum(count_comb(left-k*denominations[i], i+1) for k in range(0,(left/denominations[i])+1))


def main():
    print count_comb(total)
        

if __name__ == '__main__':
    main()