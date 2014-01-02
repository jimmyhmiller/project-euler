from math import sqrt
from heapq import heappush, heappop
import time
from functools import wraps

def memoize(f):
    f._cache = {}
    @wraps(f)
    def do_f(n):
        if n in f._cache:
            return f._cache[n]
        r = f(n)
        f._cache[n] = r
        return r
    return do_f


@memoize
def list_of_primes(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


@memoize
def prime_factors(n):
    factors = []
    nums = list_of_primes(2000)
    i = 0
    while i < len(nums) and nums[i] <= sqrt(n)+1:
        if not n % nums[i]:
            factors.append(nums[i])
            n = n/nums[i]
        else:
            i+=1
    if n != 1:
        factors.append(n)
    return factors


@memoize
def unique_prime_factors(n):
    return set(prime_factors(n))


@memoize
def prime_factors_exponents(n):
    return [(i,prime_factors(n).count(i)) for i in unique_prime_factors(n)]


@memoize
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def product(args):
    total = 1
    for i in args:
        total *= i
    return total


@memoize
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def lcm(a,b):
    return (a*b)/gcd(a, b)


@memoize
def phi(n):
    return n * product((1-1.0/i) for i in unique_prime_factors(n))


@memoize
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in xrange(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True


@memoize
def median(x):
    x.sort()
    if len(x)%2:
        return x[len(x)/2]
    else:
        return (x[len(x)/2]+float(x[len(x)/2-1]))/2


@memoize
def triangle_number(n):
    return n*(n+1)/2


@memoize
def reverse_int(x):
    return int(str(x)[::-1])


@memoize
def reverse_str(x):
    return str(x)[::-1]


@memoize
def palindrome(x):
    return str(x) == reverse_str(x)


def xdigits(n):
    while n != 0:
        a = n%10
        n /= 10
        yield(a)


@memoize
def digits(n):
    digits = []
    while n != 0:
        a = n%10
        n /= 10
        digits.append(a)
    return digits


@memoize
def decimal_to_binary(x):
    return "{0:#b}".format(x)[2:]


def sum_of_digits(x):
    return sum(digits(x))


@memoize
def proper_divisors(n):
    divs = []
    if n == 0:
        return set([0])
    if n == 1:
        return set([1])
    for i in xrange(1,int(sqrt(n))+1):
        if n % i == 0:
            divs.append(i)
            if n / i != i:
                divs.append(n/i)
    divs.remove(n)
    return set(divs)


@memoize
def divisors(n):
    return list(proper_divisors(n)) + [n]


@memoize
def num_of_divisors(n):
    return product(prime_factors(n).count(i)+1 for i in unique_prime_factors(n))


def timer(f, *args):
    t = time.time()
    result = f(*args)
    print time.time()-t
    return result


def counting_sort(seq):
    count = []
    sorted_seq = []
    for i in seq:
        while len(count) <= i:
            count.append(0)
        count[i] += 1
    for i in xrange(len(count)):
        sorted_seq.extend([i]*count[i])
    return sorted_seq


def distribute(seq):
    beads = []
    for i in seq:
        while len(beads) <= i:
            beads.append(0)
        for j in xrange(1,i+1):
            beads[j] += 1
    return beads


def bead_sort(seq):
    beads = distribute(seq)
    beads = distribute(beads)
    beads.remove(0)
    return beads


def insertion_sort(seq):
    for i in xrange(1,len(seq) ):
        key = seq[i]
        j = i-1
        while j >= 0 and seq[j] > key:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j+1] = key
    return seq


def shell_sort(seq):
    gaps = [1, 4, 10, 23, 57, 132, 301, 701]
    for gap in gaps:
        seq[::gap] = insertion_sort(seq[::gap])
    return seq


def selection_sort(seq):
    for i in range(0,len(seq)):
        min = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        if min != i:
            seq[i], seq[min] = seq[min], seq[i]
    return seq


def merge(left,right):
    temp = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    temp += (left[i:])
    temp += (right[j:])
    return temp


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    middle = len(seq)/2
    left = merge_sort(seq[:middle])
    right = merge_sort(seq[middle:])
    return merge(left,right)


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq.pop(0)
    greater = quick_sort([x for x in seq if x >= pivot])
    lesser =  quick_sort([x for x in seq if x < pivot])
    return lesser + [pivot] + greater


def bubble_sort(seq):
    sorted = False
    while not sorted:
        sorted = True
        for i in xrange(len(seq)-1):
            if seq[i] > seq[i+1]:
                sorted = False
                seq[i],seq[i+1] = seq[i+1],seq[i]
    return seq


def comb_sort(seq):
    shrink = 1.3
    gap = int(len(seq)/shrink)
    while gap >= 1:
        seq[::gap] = bubble_sort(seq[::gap])
        gap = int(gap/shrink)
    return seq

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def radix_sort(seq):
    i = 0
    while 1:
        done = True
        buckets = [[] for j in range(11)]
        for item in seq:
            if i < len(digits(item)):
                done = False
                buckets[digits(item)[i]+1].append(item)
            else:
                buckets[0].append(item)
        if done:
            break
        seq = [item for bucket in buckets for item in bucket]
        i += 1
    return seq


def binary_search(element,seq):
    low = 0
    high = len(seq)
    while low < high:
        mid = (low+high) / 2
        if seq[mid] > element:
            high = mid
        elif seq[mid] < element:
            low = mid+1
        else:
            return mid
    return -1


def main():
    to_sort = [8,2,4,9,3,6,4,3,6,7,4,12,4,32,43,300]*200
    # timer(counting_sort,to_sort[:])
    # timer(radix_sort,to_sort[:])
    # timer(heapsort, to_sort[:])
    # timer(merge_sort,to_sort[:])
    # timer(quick_sort,to_sort[:])
    # timer(bead_sort,to_sort[:])
    # timer(selection_sort,to_sort[:])
    # timer(insertion_sort,to_sort[:])
    # timer(shell_sort,to_sort[:])
    # timer(bubble_sort,to_sort[:])
    # timer(comb_sort,to_sort[:])
    timer(list_of_primes, 1000000)
if __name__ == '__main__':
    main()
