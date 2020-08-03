#!/usr/bin/python

from random import randrange

def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u==v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u
    return None
# Main Program
n = 10
G = [[randrange(2) for i in range(n)] for i in range(n)]
# Create a celeb
c = randrange(n)
for i in range(n):
    G[i][c] = True
    G[c][i] = False
print G
print naive_celeb(G)
