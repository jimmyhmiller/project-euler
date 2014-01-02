#!/usr/bin/env python

# n**2 + n**2-(n-1) + n**2 - 2(n - 1) + n**2 - 3(n - 1)
diagonal = lambda n: 4*n**2 - 6*(n-1)


def main():
    print sum(diagonal(i) for i in range(3,1002,2)) + 1


if __name__ == '__main__':
    main()