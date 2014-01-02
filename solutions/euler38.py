#!/usr/bin/env python
from util import digits


def is_pandigital(n):
    i = 1
    digits_count = [0]*10
    while digits_count.count(1) != 9:
        for digit in digits(n*i):
            if digit == 0 or digits_count[digit] > 1:
                return (False,0)
            else:    
                digits_count[digit] += 1
        i+=1
    num = "".join("".join(str(d) for d in digits(n*j)[::-1]) for j in range(1,i))
    return (True,num)


def main():
    maximum = 0
    for i in range(1,10000):
        p = is_pandigital(i)
        if p[0] == True and p[1] > maximum:
            maximum = p[1]
    print maximum
       

if __name__ == '__main__':
    main()