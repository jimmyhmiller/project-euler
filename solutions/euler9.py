#!/usr/bin/env python
"""
a = k(m**2 - n**2), b = k(2mn), c = k(m**2 + n**2)
a + b + c = 1000
k(m**2-n**2+2mn + m**2+n**2)
k(2m**2+2mn) = 1000
2km(m+n) = 1000
km(m+n) = 500
m>n
"""


def main():
    a = lambda k, m, n: k*(m**2 - n**2)
    b = lambda k, m, n: k*(2*m*n)
    c = lambda k, m, n: k*(m**2 + n**2)
    for k in range(1,500):
        for m in range(1,500):
            for n in range(1,m):
                if k*m*(m+n) == 500:
                    print a(k,m,n) * b(k,m,n) * c(k,m,n)
                    quit()
if __name__ == '__main__':
    main()