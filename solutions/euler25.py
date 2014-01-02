#!/usr/bin/env python
from util import fibonacci


def main():
    i = 1
    while fibonacci(i) < 10**999:
        i+=1
    print i


if __name__ == '__main__':
    main()