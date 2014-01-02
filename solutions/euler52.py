#!/usr/bin/env python


def multiples(x):
    for i in range(1,7):
        if sorted(list(str(x))) != sorted(list(str(x*i))):
            return False
    return True


def main():
    i = 125874
    while not multiples(i):
        i+=1
    print i


if __name__ == '__main__':
    main()