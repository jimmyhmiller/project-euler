#!/usr/bin/env python
from util import digits, timer


def fraction(l):
    x,y = 5,2
    for i in range(l-1):
        x,y = y,x
        x += y*2
    x,y = y,x
    x += y
    return x,y

        
def more_digits(x,y):
    return len(digits(x)) > len(digits(y))


def main():
    print sum(more_digits(*fraction(i)) for i in range(2,1001))


if __name__ == '__main__':
    main()