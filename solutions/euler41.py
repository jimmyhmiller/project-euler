#!/usr/bin/env python
from util import is_prime
from itertools import permutations

"""
if sum of digits is mulitple of three it is a multiple of three
sum(range(1,6)) = 15
sum(range(1,7)) = 21
sum(range(1,10)) = 45
Must start with 7
"""


num = "7"


def main():
    ans = 0
    for i in permutations("123456"):
        temp = int(num+"".join(i))
        if is_prime(temp) and temp > ans :
            ans = temp
    print ans


if __name__ == '__main__':
    main()