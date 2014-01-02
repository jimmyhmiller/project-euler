#!/usr/bin/env python
from util import xdigits


def is_pandigital(n):
    if len(n) != 9:
        return False
    elif "0" in n:
        return False
    else:
        return len(set(n)) == 9


def main():
    nums = [0]*1000000
    total = 0
    for i in range(5000):
        for j in range(i):
            if is_pandigital(str(i) + str(j) + str(i*j)):
                if nums[i*j] == 0:
                    total += i*j
                nums[i*j] += 1
    print total
        

if __name__ == '__main__':
    main()