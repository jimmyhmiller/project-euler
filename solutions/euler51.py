from util import list_of_primes, digits


primes = set(str(p) for p in list_of_primes(1000000))


def count(number):
    return set(d for d in number[:-1] if number[:-1].count(d) > 1)


def replace_digit(prime,digit,i):
    return prime[:-1].replace(digit,i) + prime[-1]


def all_possible(prime,d):
    return [replace_digit(prime,d,str(i)) for i in range(10) if replace_digit(prime,d,str(i)) in primes]
 

def main():
    for p in primes:
        for digit in count(p):
            chain = all_possible(p,digit)
            if len(chain) == 8:
                print chain
                exit()   

