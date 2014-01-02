#!/usr/bin/env python
from math import sqrt


def hexagonal(n):
    return n*(2*n-1)


def pentagonal_test(x):
    return (sqrt(24*x+1) + 1) % 6 == 0


def main():
    n = 144
    while not pentagonal_test(hexagonal(n)):
        n+=1
    print hexagonal(n)


if __name__ == '__main__':
    main()