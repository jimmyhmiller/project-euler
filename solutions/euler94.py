#!/usr/bin/env python
from math import sqrt


def area(a,c):
    return sqrt(a**2 - (.5*c)**2) * .5*c % 1 == 0


def main():
    a = 1
    c = 2
    total = 0
    while a**2 + c <= 1000000000:
        if area(a,c):
            total += a**2 + c
        a += 1
        c += 1
    a += 2
    while c >= 1:
        if area(a,c):
            total += a**2 + c
        a -= 1
        c -= 1
    print total


if __name__ == '__main__':
    main()