from util import sum_of_digits

e = []
k = 1
while len(e) < 99:
    e.extend([1,2*k,1])
    k+=1
e = e[:99][::-1]


def main():
    x,y = 1,e[0]
    x += y*e[1]
    for i in e[2:]:
        x,y = y,x
        x += y*i
    x,y = y,x
    x += 2*y
    print sum_of_digits(x)
        


if __name__ == '__main__':
    main()