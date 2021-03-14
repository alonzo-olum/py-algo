#!/bin/env python

def dfs_topsort(G):
    S, res = set(), []      # History & result
    def recurse(u):         # Traversal subroutine
        if u in S: return   # Already visited, Ignore
        S.add(u)            # Visit node
        for v in G[u]:      # Explore its neighbours
            recurse(v)      # Traverse the neighbour as parent
        res.append(u)       # Finished with u: Append to result
    for u in G:
        print ("u in ts {}".format(u))
        recurse(u)          # Cover the entire graph
    res.reverse()           # dfs ends up backwards for desc finish times so
    return res

# Main Program
#a, b, c, d, e, f, g, h = range(8)
#G = [
#        {b, c, d, e, f},    #a
#        {c, e},             #b
#        {d},                #c
#        {e},                #d
#        {f},                #e
#        {c, g, h},          #f
#        {f, h},             #g
#        {f, g}              #h
#        ]
#print (dfs_topsort(G))
