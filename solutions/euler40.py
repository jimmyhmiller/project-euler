#!/usr/bin/env python
from util import product


def concat_digit():
    digit = "0"
    i = 1
    while len(digit) <= 1000000:
        digit += str(i)
        i += 1
    return digit


def main():
    digits = concat_digit()
    print product(int(digits[10**i]) for i in range(6))


if __name__ == '__main__':
    main()