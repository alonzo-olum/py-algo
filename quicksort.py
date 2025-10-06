#!/bin/env python3

from randomized_select import RandomizedSelect

def quicksort(seq):
    if len(seq) <= 1: return seq
    lo, pi, hi = RandomizedSelect.partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

if __name__ == '__main__':
    seq = [6, 3, 7, 1, 9, 2, 5]
    print(quicksort(seq))
