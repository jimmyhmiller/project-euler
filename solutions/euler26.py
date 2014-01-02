#!/usr/bin/env python
from decimal import Decimal as D
from decimal import getcontext
getcontext().prec = 2000


def find_pattern(num):
    if len(num)+20 < getcontext().prec:
        return 0
    i = 1
    while num[0:i] != num[i:i*2]:
        i+=1
    return i


def main():
    nums = [str(D(1)/D(i))[::-1][20:] for i in range (2,1000)]
    nums = [find_pattern(i) for i in nums]
    print nums.index(max(nums)) + 2


if __name__ == '__main__':
    main()