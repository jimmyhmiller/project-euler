#!/usr/bin/env python
from util import proper_divisors


def abundant(n):
    return sum(proper_divisors(n)) > n


def abundantsum(i, all_abundants):
    return any(i-a in all_abundants for a in all_abundants)


def main():
    all_abundants = set(i for i in range(1,28123) if abundant(i))
    print sum(i for i in range(1,28123) if not abundantsum(i, all_abundants))


if __name__ == '__main__':
    main()