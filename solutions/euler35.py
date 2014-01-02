#!/usr/bin/env python
from util import list_of_primes


primes = [str(p) for p in list_of_primes(1000000)]


def rotate(str):
    for i in range(len(str)):
        str = str[1:] + str[0]
        yield str


def remove_evens():
    temp_primes = []
    for s in primes:
        if "2" not in s and "4" not in s and "6" not in s and "8"\
                not in s and "0" not in s and "5" not in s:
            temp_primes.append(s)
    return temp_primes


def main():
    temp_primes = []  
    for s in remove_evens():
        for r in rotate(s):
            if r not in primes:
                break
        else:
            temp_primes.append(s)    
    print len(temp_primes) + 2

if __name__ == '__main__':
    main()