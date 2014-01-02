from util import unique_prime_factors, product

def rad(n):
    return product(unique_prime_factors(n))


def main():
    print sorted((rad(i),i) for i in range(1,100001))[9999]


if __name__ == '__main__':
    main()
