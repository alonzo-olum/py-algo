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
    for u in G[2]:
        if u in seen: continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp

# Main program
a, b, c, d, e, f, g, h  = range(8)
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
#print(walk(G, c))
print (components(G))
