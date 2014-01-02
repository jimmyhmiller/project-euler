#!/usr/bin/env python
from math import sqrt


def main():
    perimeter = [0]*1001
    for a in range(500):
        for b in range(500-a):
            c = sqrt(a**2+b**2)
            if int(c) == c:
                perimeter[int(a+b+c)] += 1
    print perimeter.index(max(perimeter))


if __name__ == '__main__':
    main()