#!/bin/env python3

from collections import Counter
import cProfile

def anagram(first_string, second_string):
    if Counter(first_string) == Counter(second_string):
        return True
# Main Program Block
first_string = "debit card"
second_string = "bad credit"
print(anagram(first_string, second_string))
#print(cProfile.run('anagram(first_string, second_string))')
