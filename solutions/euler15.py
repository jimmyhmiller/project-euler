#!/usr/bin/env python


def memoize(f):
    f._cache = {}
    def do_f(x,y):
        if (x,y) in f._cache:
            return f._cache[(x,y)]
        r = f(x,y)
        f._cache[(x,y)] = r
        return r
    return do_f


@memoize
def find_routes(x,y):
    routes = 0
    if x == 0 and y == 0:
        routes += 1
    if x > 0:
        routes += find_routes(x-1,y)
    if y > 0:
        routes += find_routes(x,y-1)
    return routes

def main():
    print find_routes(200,200)


if __name__ == '__main__':
    main()