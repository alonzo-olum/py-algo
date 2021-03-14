#!/bin/env python3

from dfs_topsort import dfs_topsort
from fcc import walk

def tr(G):                                      # Transpose (reverse edges) G
    GT = dict()
    for u in G: GT[u] = set()                   # Initialize all nodes in G
    for u in G:                 
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT = tr(G)                                  # Get the transposed graph
    print ("transposed G %s") % (GT)
    sccs, seen = [], set()
    for u in dfs_topsort(G):                     # DFS starting point
        print ("dfs_ts %d") % (u)
        if u in seen: continue
        C = walk(GT, u, seen)                   # Don't go "backwards" (seen)
        seen.update(C)                          # Seen traversal C
        sccs.append(C)                          # Add to components
    return sccs

# Main Block
a, b, c, d, e, f, g, h, i = range(9)
G = {
        a: [b, c],                  #a
        b: [d, e, i],               #b
        c: [d],                     #c
        d: [a, h],                  #d
        e: [f],                     #e
        f: [g],                     #f
        g: [e, h],                  #g
        h: [i],                     #h
        i: [h]                      #i
        }
print (scc(G))
