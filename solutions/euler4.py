#!/usr/bin/env python
from util import palindrome


def main():
    three_digit_prods = [x*y for x in range(100,1000) for y in range(100,1000)]
    print max(i for i in three_digit_prods if palindrome(i))
    
    
if __name__ == '__main__':
    main()