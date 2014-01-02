#!/usr/bin/env python
from string import ascii_uppercase as alphabet

def process_file(f):
    data = f.read()
    data = data.replace("\"", "")
    data = data.split(",")
    data.sort()
    return data


def name_score(name,i):
    return sum(alphabet.index(a)+1 for a in name)*(i+1)

def main():
    f = open("euler22.txt", "r")
    data = process_file(f)
    print sum(name_score(name,i) for i,name in enumerate(data))
        


if __name__ == '__main__':
    main()