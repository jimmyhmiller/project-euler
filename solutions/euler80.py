from decimal import *
from math import sqrt
from util import sum_of_digits
getcontext().prec = 105

def main():
    total = 0
    for i in range(1,101):
        num = str(Decimal(i).sqrt())[:-5].replace(".","")
        if len(num) == 100:
            total += sum_of_digits(int(num))
    print total

if __name__ == '__main__':
    main()