#!/usr/bin/env python3

from random import randrange
from random import randint
from collections import defaultdict

# index keys 0,1,2,3 as airports in a dictionary
# random integral values 0-8 representing hours to the airport
def init_A(n):
    a,b,c,d=range(n)
    return {a: randrange(2*n), b: randrange(2*n), c: randrange(2*n), d: randrange(2*n)}

# dictionary of a list of dictionaries
# key indexing to represent airport
# value is a list of {town: time} in a dict
def init_B(n):
    B = defaultdict(list)
    for i in range(n):
        for j in range(n, 2*n+1):
            B[i].append({j: randint(1,9)})
    return B

# initial C is allocated max float values
# will harbor the minimum time to get to town v
def init_C(n):
    C = dict()
    for i in range(n, 2*n+1):
        C[i] = float('inf')
    return C

# randomized way of estimating time it will take to get to town v
def relaxation(A, B, C, n, N):
    for i in range(N):
        u, v = randrange(n), randint(n, 2*n+1)
        for j in B[u]:
            if j.get(v) is not None:
                C[v] = min(C[v], A[u]+j[v])
    return C

# main block
n=4
N=120
A=init_A(n)
B=init_B(n)
C=init_C(n)

print(relaxation(A, B, C, n, N))
