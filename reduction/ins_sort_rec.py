#!/usr/bin/python

def ins_sort_rec(seq, i):
    if i==0: return
    ins_sort_rec(seq, i-1)
    j=i
    while j>0 and seq[j-1]>seq[j]:
	    seq[j-1],seq[j]=seq[j],seq[j-1]
	    j-=1
    return seq
# main program
sequence=[13,2,9,3,7,4,6,5,1,8,10,12,11]
len_of_sequence = len(sequence)
print ins_sort_rec(sequence,len_of_sequence-1)
