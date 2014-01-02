from util import prime_factors, unique_prime_factors

def pascal(x):
    triangle = [[1],[1,1]]
    for i in range(x-2):
        triangle.append([1])
        for j in range(1,len(triangle[-2])):
            triangle[-1].append(triangle[-2][j-1] + triangle[-2][j])
        triangle[-1].append(1)
    return triangle

def square_free(x):
    return len(prime_factors(x)) == len(unique_prime_factors(x))

def main():
    distinct_pascal = set([n for r in pascal(51) for n in r])
    print sum(n for n in distinct_pascal if square_free(n))

if __name__ == '__main__':
    main()