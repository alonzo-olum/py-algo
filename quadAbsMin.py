#!/usr/bin/python

def absolute_min(list):
    m = float('inf')
    for x in list:
        for y in list:
            if x == y: continue
            d=abs(x - y)
            if d < m:
                xx, yy, m=x, y, d

    return xx, yy
# main prog
items = [3, 6, 2, 5, 1, 7, 4, 2, 8, 9, 12]
xx, yy = absolute_min(items)
print "abs min: x {} y {} ".format(xx, yy)
