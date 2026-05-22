#!/bin/python3
# Finding Connected Components - (FCC)

# walk returns a predecessor map as a traversal tree
def walk(G, s, S=set()):
    P, Q = dict(), set()                        # Predecessors + "to do" queue
    P[s] = None                                 # starting node has no predecessors
    Q.add(s)                                    # add starting node to do
    while Q:                                    # Still nodes to visit
        u = Q.pop()                             # Pick last inserted node
        for v in G[u].difference(P, S):         # new nodes?
            Q.add(v)                            # add neighbours to do
            P[v] = u                            # We know its predecessor
        return P                                # Traversal tree

def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp

# Main program
#a,b,c,d,e,f,g,h = range(8)
#G = {
#        a: { b, d },
#        b: { c, d },
#        c: { f, g, h},
#        d: { e, g },
#        e: { f, h },
#        f: { h },
#        g: { e, h },
#        h: set()
#    }
#print(components(G))
