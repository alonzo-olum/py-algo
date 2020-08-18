#!/bin/env python3

def topsort(G):
    count = dict((u, 0) for u in G)         # in degrees for each node
    for u in G:
        for v in G[u]:
            count[v] += 1                   # count dependent neighbours (in-edge) (from v's perspective)
    Q = [u for u in G if count[u] == 0]     # dependency nodes (initial nodes)
    S = []
    while Q:                                # While we have start nodes ....
        u = Q.pop()                         # Pick one
        S.append(u)                         # Use is as first of rest
        for v in G[u]:
            count[v] -= 1                   # "Uncount" its out edges (from u's perspective)
            if count[v] == 0:               # New valid start nodes?
                Q.append(v)                 # Queue it next
    return S
