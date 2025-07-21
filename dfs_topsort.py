#!/bin/env python3

def dfs_topsort(G):
    S, res = set(), []      # History & result
    def recurse(u):         # Traversal subroutine
        if u in S: return   # Already visited, Ignore
        S.add(u)            # Visit node
        for v in G[u]:      # Explore its neighbours
            recurse(v)      # Traverse the neighbour as parent
        res.append(u)       # Finished with u: Append to result
        print("[recurse]: %s" % (res))
    for u in G:
        recurse(u)          # Cover the entire graph
    res.reverse()           # dfs ends up backwards for desc finish times so
    return res

# Main Program
#a, b, c, d, e, f, g, h = range(8)
#G = {
#        a: {b, c, d, e, f},    #a
#        b: {c, e},             #b
#        c: {d},                #c
#        d: {e},                #d
#        e: {f},                #e
#        f: {c, g, h},          #f
#        g: {f, h},             #g
#        h: {f, g}              #h
#        }
#print (dfs_topsort(G))
