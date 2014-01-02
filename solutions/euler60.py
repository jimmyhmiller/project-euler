from util import list_of_primes



def main():
    primes = [str(p) for p in list_of_primes(10000)]
    s_primes = set(str(p) for p in list_of_primes(1000000))
    primes = [p for p in primes if p[-1] != "2" or p[-1] != "5"]

    con = [p1+p2 for p1 in primes for p2 in primes]
    con = [c for c in con if c in s_primes]

    print con


if __name__ == '__main__':
    main()