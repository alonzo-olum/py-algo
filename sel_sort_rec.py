#!/usr/bin/env python

def sel_sort_rec(seq, i):
    if i==0: return
    max_j=i
    for j in range(i):
        if seq[j]>seq[max_j]: max_j=j
    seq[i],seq[max_j]=seq[max_j],seq[i]
    sel_sort_rec(seq,i-1)
    return seq

# Main Program
sequence=[11,4,9,2,10,7,5,1,6,8,3]
print sel_sort_rec(sequence,len(sequence)-1)
