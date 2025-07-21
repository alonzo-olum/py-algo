#!/usr/bin/env python3

def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P

# main block
a,b,c,d,e,f,g,h = range(8)
G = {
        a: { b, d },
        b: { c, d },
        c: { f, g, h},
        d: { e, g },
        e: { f, h },
        f: { h },
        g: { e, h },
        h: set()
    }
print(walk(G, a))
