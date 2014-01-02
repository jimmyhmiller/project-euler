#!/usr/bin/env python
from util import factorial


nCr = lambda n,r: factorial(n)/(factorial(r)*factorial(n-r))


def main():
    total = 0
    for n in range(23,101):
        for r in range(1,n+1):
            if nCr(n,r) > 1000000:
                total += 1
    print total
            

if __name__ == '__main__':
    main()