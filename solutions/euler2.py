#!/usr/bin/env python
from util import fibonacci as fib
    
def main():
    i = 1
    total = 0
    while fib(i) < 4000000:
        if fib(i) % 2 == 0:
            total += fib(i)
        i+=1
    print total

if __name__ == '__main__':
    main()