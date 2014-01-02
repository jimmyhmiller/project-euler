#!/usr/bin/env python
from util import factorial, digits


def main():
    print sum(i for i in range(3,50000) if sum(factorial(d) for d in digits(i)) == i)


if __name__ == '__main__':
    main()