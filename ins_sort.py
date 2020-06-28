#!/usr/bin/python

def ins_sort(seq):
    for i in range(1, len(seq)):
        j=i
        while j>0 and seq[j-1]>seq[j]:
            seq[j-1],seq[j]=seq[j],seq[j-1]
            j-=1
    return seq

# Main Program:
sequence=[5,2,8,6,1,3,9]
print ins_sort(sequence)
