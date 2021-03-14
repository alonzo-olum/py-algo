#!/bin/env python3

from random import randrange

def relaxation(n, N):
    A = [randrange(n) for i in range(N)]
    B = [[randrange(n) for i in range(N)] for i in range(N)]
    C = range(n)
    for v in range(n):
        C[v] = float('inf')
    for i in range(N):
        u, v = randrange(n), randrange(n)
        print("u: %d --- v: %d") % (u, v)
        C[v] = min(C[v], A[u]+B[u][v])  #Relax
        print("C[v] = %d :: B[u][v] = %d :: A[u] = %d") % (C[v], B[u][v], A[u])
        print("C: %s") % (C)
        print("B: %s") % (B)
        print("A: %s") % (A)
    return min(C)

# Main Program

print("min route %d") % (relaxation(8, 8))
