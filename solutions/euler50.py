#!/usr/bin/env python
from util import list_of_primes


primes = list_of_primes(1000000)
sprimes = set(primes)


def main():
    max_chain = 0
    num = 0
    for i in range(len(primes)):
        j = i
        while j < len(primes):
            n = sum(primes[i:j])
            if n > 1000000:
                break
            if n in sprimes and j-i > max_chain:
                max_chain = j-i
                num = n
            j+=1
    print max_chain, num


if __name__ == '__main__':
    main()