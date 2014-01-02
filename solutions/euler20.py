#!/usr/bin/env python
from util import factorial
        
def main():
    print sum(int(i) for i in str(factorial(100)))


if __name__ == '__main__':
    main()