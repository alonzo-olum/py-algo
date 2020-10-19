#!/bin/env python3

def recursive_dfs(G, s, S=None):
    if S is None: S = set()                 # Initialize the history ( visited )
    S.add(s)                                # Add visited node s
    for u in G[s]:                          # traverse neighbours
        if u in S: continue                 # Already visited ? Skip
        recursive_dfs(G, u, S)              # New: Explore recursively
    return S

# Main Program
a, b, c, d, e, f, g, h = range(8)
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
print(recursive_dfs(G, a))
