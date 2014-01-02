#!/usr/bin/env python
from util import proper_divisors as pro_divs

def main():
    total = 0
    for a in range(2,10000):
        b = sum(pro_divs(a))
        if a != b and sum(pro_divs(b)) == a:
            total += a + b
    print total/2


if __name__ == '__main__':
    main()