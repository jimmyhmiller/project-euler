#!/usr/bin/env python
from util import phi

def main():
    temp = [i/phi(i) for i in range(1,1000001)]
    print temp.index(max(temp)) + 1
        
if __name__ == '__main__':
    main()