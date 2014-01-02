#!/usr/bin/env python

"""
xy/yz = x/z
(10*x+y)/(10*y+z) = x/z
x != y
"""


def main():
    total = 1
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                x,y,z = x*1.,y*1.,z*1.
                if (10*x+y)/(10*y+z) == x/z and x!=y:
                    total *= x/z
    print total


if __name__ == '__main__':
    main()