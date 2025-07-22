#!/bin/env python3

def max_perm(M):
    n=len(M)
    A=set(range(n))
    count=[0]*n
    for i in M:
        count[i]+=1
    Q=[i for i in A if count[i]==0]
    while Q:
        j=Q.pop()
        A.remove(j)
        k=M[j]
        count[k]-=1
        if count[k]==0:
            Q.append(k)
    return A

# Main Program
M=[2,2,0,5,3,5,7,4]
print max_perm(M)
