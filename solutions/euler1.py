#!/usr/bin/env python


def main():
    print sum(i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0)


if __name__ == '__main__':
    main()
