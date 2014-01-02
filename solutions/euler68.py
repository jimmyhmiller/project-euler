#!/usr/bin/env python

triangle = open("triangle.txt","r").read()
triangle = [[int(j) for j in i.split()] for i in triangle.split("\n")]

def main():
    for r in range(len(triangle) -2, -1, -1):
        for c in range(len(triangle[r])):
            if triangle[r+1][c] > triangle[r+1][c+1]:
                triangle[r][c] += triangle[r+1][c]
            else:
                triangle[r][c] += triangle[r+1][c+1]
    print triangle[0][0]


if __name__ == '__main__':
    main()