#!/usr/bin/env python


def main():
    print sum(len(str(i**j)) == j for i in range(1,22) for j in range(1,22))


if __name__ == '__main__':
    main()