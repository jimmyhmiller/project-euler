#!/usr/bin/env python
def sum_of_digits(x):
    return sum(int(i) for i in str(x))


def main():
    print max(sum_of_digits(a**b) for a in range(2,100) for b in range(2,100))


if __name__ == '__main__':
    main()