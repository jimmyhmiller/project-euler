#!/usr/bin/env python
from util import decimal_to_binary, palindrome


def main():
    print sum(i for i in range(1000000) if palindrome(i) and palindrome(decimal_to_binary(i)))


if __name__ == '__main__':
    main()