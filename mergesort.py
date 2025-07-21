#!/usr/bin/env python3

def mergesort(seq):
    mid = len(seq)//2
    lft,rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res=[]
    while lft and rgt:
        if lft[-1] > rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

# main block
seq=[12, 34, 1, 5, 7, 3, 23, 13, 123, 4]
print(mergesort(seq))
