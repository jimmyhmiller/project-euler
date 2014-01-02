from util import digits

def bouncy(x):
    digs = digits(x)
    up, down = False, False
    for i in range(1,len(digs)):
        if digs[i-1] < digs[i]:
            down = True
        elif digs[i-1] > digs[i]:
            up = True
        if up and down:
            return True
    return False

def main():
    total = 0.
    for i in range(1,10000000):
        if bouncy(i):
            total += 1
        if total/i >= .99:
            print i,total
            break

if __name__ == '__main__':
    main()