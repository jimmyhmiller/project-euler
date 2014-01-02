#!/usr/bin/env python
from util import palindrome, reverse_int


def lychrel(x):
    for i in range(50):
        x += reverse_int(x)
        if palindrome(x):
            return False
    return True


def main():
    print sum(1 for i in range(1,10000) if lychrel(i))
        

if __name__ == '__main__':
    main()