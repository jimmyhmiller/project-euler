#!/usr/bin/env python
from math import sqrt


def num_of_prime_factors(n):
    n_factors = [0]*n 
    for i in xrange(2,int(sqrt(len(n_factors))+1)): 
        if n_factors[i] == 0: 
            for j in xrange(i*2,n,i):
                n_factors[j] +=1
    return n_factors


def main():
	factors = num_of_prime_factors(1000000)
	count = 0
	for i in range(len(factors) - 4):
	    if factors[i] == 4 and len(set(factors[i:i+4])) == 1:
	        print i
	        exit()


if __name__ == '__main__':
	main()