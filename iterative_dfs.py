#!/bin/env python3

def iterative_dfs(G, s):
    S, Q = set(), []                # History & Queue
    Q.append(s)                     # we plan on starting node s
    while Q:                        # we have nodes to do
        u = Q.pop()                 # pick one
        if u in S: continue         # already visited we can skip
        S.add(u)                    # If not we have it now
        Q.extend(G[u])              # schedule all neighbours
        yield u                     # report u as done

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
print(list(iterative_dfs(G, a)))
