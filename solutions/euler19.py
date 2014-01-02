#!/usr/bin/env python
import datetime

def main():
    print sum(1 for y in range(1901,2001) for m in range(1,13) if datetime.date(y,m,1).weekday() == 6)

if __name__ == '__main__':
    main()