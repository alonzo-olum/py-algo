#!/bin/env python3

def max_interval(seq):
    n = len(seq)
    best = seq[0]
    for sz in range(1, n+1):
        cur = sum(seq[:sz])
        for i in range(n-sz):
            cur += seq[i+sz] - seq[i]
            best = max(best, cur)
    return best

if __name__ == '__main__':
    A = [i for i in range(10, 19)]
    print(max_interval(A))
