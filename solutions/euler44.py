#!/usr/bin/env python
from math import sqrt


pent = [n*(n*3-1)/2 for n in range(1,3000)]
test = lambda x: (sqrt(24*x +1) + 1) % 6 


def main():
    for i in range(len(pent)):
        for j in range(i):
            if test(pent[i]-pent[j]) == 0 and test(pent[i]+pent[j]) == 0:
                print pent[i]-pent[j]
                break

if __name__ == '__main__':
    main()