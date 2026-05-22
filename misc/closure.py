#!/bin/env python3

def mulliplier(f):
    def multiply(x):
        return x * f
    return multiply

triple = mulliplier(3)
print(triple(4))
