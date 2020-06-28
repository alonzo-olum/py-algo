#!/usr/bin/env python

from random import randrange

def celeb(G):
    # length of graph
    n=len(G)
    # first two
    u, v=0, 1
    # others check
    for c in range(1,n+1):
        # u knows v replace u
        if G[u][v]: u = c
        # else replace v
        else: v = c
    # after all u replaced last use v
    if u == n: c = v
    # else v replaced last use u
    else: c = u
    # For everyone else
    for v in range(n):
        # same person as v == v
        if c == v: continue
        # candidate knows other
        if G[c][v]: break
        # else other doesnt know candidate
        if not G[v][c]: break
    else:
        return c
    return None

# Main Programs
n=100
G=[[randrange(2) for i in range(n)] for i in range(n)]
# create a celeb
c=randrange(n)
for i in range(n):
    G[i][c]=True
    G[c][i]=False
# call our func
print ("\n%s") % (G)
print celeb(G)
