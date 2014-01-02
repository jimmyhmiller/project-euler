from util import list_of_primes

def all_perms(s):
    if len(s) ==1:
        yield s 
    else:
        for perm in all_perms(s[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + s[0] + perm[i:]

   
primes = list_of_primes(10000)
primes = [p for p in primes if p >=1000]
sprimes = set(str(p) for p in primes)

def filter():
    for s in sprimes:
        total = 0
        for p in all_perms(s):
            if p in sprimes:
                total+=1
            if total >= 3:
                break
        else:
            primes.remove(int(s))

def main():
    for p in primes:
        for q in primes:
            d = abs(q-p)
            if q>p and set(str(p)) == set(str(q)) and q+d in primes and set(str(q+d)) == set(str(q)):
                print p,q,q+d,d


if __name__ == '__main__':
    main()


