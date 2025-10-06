#!/bin/env python

def fibonacci():
    x,y=0,1
    while(True):
        yield y
        x,y=y,x+y

# main program
f = fibonacci()
for r in range(5):
    print f.next()
