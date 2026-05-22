#!/bin/env python3

def dfs_ts(G, s, d, f, S=None, t=0):
    if S is None: S = set()             # Initialize the history
    d[s] = t; t += 1                    # Set discovery time
    S.add(s)                            # Add s to visited
    for u in G[s]:                      # Explore its neighbours
        if u in S: continue             # if already visited neighbour, Skip
        t = dfs_ts(G, u, d, f, S, t)    # Recurse; updating timestamp
    f[s] = t; t += 1                    # Set finish time
    return t                            # return timestamp

# Main Program
a, b, c, d, e, f, g, h = range(8)
discovery = dict()
finish = dict()
G = [
        {b, c, d, e, f},    #a
        {c, e},             #b
        {d},                #c
        {e},                #d
        {f},                #e
        {c, g, h},          #f
        {f, h},             #g
        {f, g}              #h
        ]
print(dfs_ts(G, a, discovery, finish))
