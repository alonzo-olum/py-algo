#!/bin/env python3

from collections import deque

def search(lines, pattern, history=5):
    prev = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev
        prev.append(line)

# main code block

if __name__ == '__main__':
    with open("") as f:
        for line, prev in search(f, 'pattern'):
            for pline in prev:
                print(pline)
            print(line)
            print('-'*20)
