#!/usr/bin/env python
from util import lcm

def main():
    l = lcm(20,19)
    for i in range(18,0,-1):
        l = lcm(l,i)
    print l

if __name__ == '__main__':
    main()