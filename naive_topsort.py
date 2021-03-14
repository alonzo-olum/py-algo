#!/bin/env python3

def naive_topsort(G, S=None):
    if S is None: S = set(G)            # Default nodes
    print("S: {}".format(S))
    if len(S) == 1: return list(S)      # Base Case, single node
    v = S.pop()                         # Reduction, remove a node
    seq = naive_topsort(G, S)           # Recursion (assumption), n-1
    print("seq: {}".format(seq))
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i = i+1       # After all dependencies
    seq.insert(min_i, v)
    return seq

a, b, c, d, e, f, g = range(7)
G = [
        [b, f],         #a
        [c, d],         #b
        [d],            #c
        [e],            #d
        [f],            #e
        []              #f
        ]
print naive_topsort(G[a])
