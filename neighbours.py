#!/bin/env python3

a, b, c, d, e, f, g, h = range(8)

    # a b c d e f g h

N = [[1,1,1,1,1,1,0,0], #a
     [0,0,1,0,1,0,0,0], #b
     [0,0,0,1,0,0,0,0], #c
     [0,0,0,0,1,0,0,0], #d
     [0,0,0,0,0,1,0,0], #e
     [0,0,1,0,0,0,1,1], #f
     [0,0,0,0,0,0,0,1], #g
     [0,0,0,0,0,1,1,1]] #h

print ("g is incident to b: %s") % ( True if N[g][b] else False)
 
print ("degrees of a is: %d") % (sum(N[a]))
