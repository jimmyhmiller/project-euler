#!/usr/bin/env python
from itertools import permutations


substrings = [(2, 5), (4, 7), (5, 8), (6, 9), (7, 10)]
nums = [3,7,11,13,17]
is_divisible = lambda x, y: x % y == 0

def has_substring(x):
    for i,s in enumerate(substrings):
        if not is_divisible(int(x[s[0]:s[1]]), nums[i]):
            return False
    return True

def main():
    total = 0
    evens = set(["0","2","4","6","8"])
    fives = set(["0","5"])
    for p in permutations("0123456789"):
        if p[3] in evens and p[5] in fives:
            p = "".join(p)
            if has_substring(p):
                total += int(p)
                
    print total


if __name__ == '__main__':
    main()