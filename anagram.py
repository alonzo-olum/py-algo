#!/bin/env python3

from collections import Counter
import cProfile

def anagram(first_string, second_string):
    if Counter(first_string) == Counter(second_string):
        return True
# Main Program Block
first_string = "algorithm"
second_string = "logarithm"
print(anagram(first_string, second_string))
#print(cProfile.run('anagram(first_string, second_string))')
