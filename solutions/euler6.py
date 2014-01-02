#!/usr/bin/env python


def main():
    sum_of_squares = sum(x**2 for x in range(1,101))
    square_of_sums = sum(range(1,101))**2
    print abs(sum_of_squares - square_of_sums)


if __name__ == '__main__':
    main()