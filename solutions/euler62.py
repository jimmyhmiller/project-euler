from util import digits
from collections import defaultdict
from itertools import izip


def main():
    cubes = [str(x**3) for x in range(10000)]
    unique_digits = ["".join(sorted(list(set(c)))) for c in cubes]
    counts = ["".join([str(cubes[i].count(d)) for d in unique_digits[i]]) for i in range(len(cubes))]

    nums = [d+c for d,c in izip(unique_digits,counts)]

    counter = defaultdict(int)

    for d in nums:
        counter[d] += 1
        
    for k in counter.keys():
        if counter[k] == 5:
            print cubes[nums.index(k)]

if __name__ == '__main__':
    main()