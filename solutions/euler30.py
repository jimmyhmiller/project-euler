#!/usr/bin/env python
from util import digits


def power_of_digits(n,p):
    return sum(i**p for i in digits(n))
        

def main():
    print sum(i for i in range(2,200000) if power_of_digits(i,5) == i)


if __name__ == '__main__':
    main()