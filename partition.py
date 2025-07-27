#!/bin/env python3

class RandomizedSelect:
    
    def __init__(self):
        pass

    @staticmethod
    def partition(seq):
        pivot, seq = seq[0], seq[1:]            # Pick and remove the pivot
        low = [s for s in seq if s <= pivot]    # all the small elements
        high = [s for s in seq if s > pivot]    # all the large ones
        return low, pivot, high                 # pivot is in the right place

    @staticmethod
    def select(seq, k):
        low, pivot, high = partition(seq)       # [<=pivot], pivot, [>pivot]
        enum_low = len(low)
        if enum_low == k: return pivot          # we found the kth smallest
        elif enum_low < k:                      # too far to the left
            return select(high, k-m-1)          # remember to adjust k
        else:
            return select(low, k)               # use the original k
