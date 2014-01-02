#!/usr/bin/env python
from string import ascii_uppercase as alphabet


def word_score(word):
    return sum(alphabet.index(a) + 1 for a in word)


def main():
    f = open("euler42.txt", "r")
    words = f.read().replace("\"","").split(",")
    scores = [word_score(word) for word in words]
    triangles = [x*(x+1)/2 for x in range(1,20)]
    print sum(1 for s in scores if s in triangles)


if __name__ == '__main__':
    main()