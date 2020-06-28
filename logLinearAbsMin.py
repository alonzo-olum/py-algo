#!/usr/bin/python

def sort_abs_min(ls):
    ls.sort()
    dd=float('inf')
    for i in range(len(ls)-1):
        x, y = ls[i], ls[i+1]
        d=abs(x-y)
        if d < dd:
            xx, yy, dd=x, y, d
    return xx, yy

# main program
list=[3,5,1.2,4.3,3.3,2.6,5.1,6,7.8,6.6]
print sort_abs_min(list)
