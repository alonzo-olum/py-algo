#!/bin/env python3

from collections import deque

def bfs(G, s):
    P, Q = {s: None}, deque([s])            # Predecessors & FIFO queue
    while Q:
        u  = Q.popleft()                    # Constant-time for deque
        for v in G[u]:
            if v in P: continue             # Has Parent set
            P[v] = u                        # Remember where we came from
            Q.append(v)
    return P

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

P = bfs(G, a)
path = [b]
while P[b] is not None:
    path.append(P[b])
    print path
    b = P[b]
print path.reverse()
