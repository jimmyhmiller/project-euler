#!/usr/bin/env python

def next(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1


cache = {}
   

def chain(n):
    if n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        c = chain(next(n))
        cache[n] = c + 1
        return c + 1


def main():
    total = [chain(i) for i in range(2,1000000)]
    print total.index(max(total))+2


if __name__ == '__main__':
    main()