#!/bin/env python3

from collections import defaultdict

def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C)+1):
        print("key val: %s") % (C[k])
        B.extend(C[k])
    return B

# main program
A = [2, 9, 3, 6, 2, 1, 8, 13, 21, 12, 15, 18, 11, 14, 10]
print counting_sort(A)
