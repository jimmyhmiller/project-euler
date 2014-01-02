#!/usr/bin/env python
from util import num_of_divisors, triangle_number


def main():
    i = 1
    while 1:
        if num_of_divisors(triangle_number(i)) > 500:
            print triangle_number(i)
            break
        i += 1


if __name__ == '__main__':
    main()