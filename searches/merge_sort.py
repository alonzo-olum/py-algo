#!/usr/bin/python

def mergesort(sequence):
    mid=len(sequence)//2
    left, right=sequence[:mid], sequence[mid:]
    if len(left) > 1: left=mergesort(left)
    if len(right) > 1: right=mergesort(right)

    res=[]
    while left and right:
        if left[-1] > right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res

# Main Program

sq = [5,2,4,11,23,6,7,9,3,1,15,18,17,14,10]
print "0(nlg n) %s:" % mergesort(sq)
