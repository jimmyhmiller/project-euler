#!/usr/bin/env python
from itertools import permutations


def main():
    print ["".join(i) for i in permutations("0123456789")][1000000]


if __name__ == '__main__':
    main()