#!/usr/bin/env python

def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j=i
        for j in range(i):
            if seq[j]>seq[max_j]: max_j=j
        seq[i], seq[max_j]=seq[max_j], seq[i]
    return seq

# More Programs
sequence=[5,10,9,2,7,1,6,11,4,8,3]
print sel_sort(sequence)
