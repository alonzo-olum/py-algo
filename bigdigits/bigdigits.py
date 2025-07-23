#!/usr/bin/python

import sys

Digits=[
        [" *** ", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "],      #Zero
        [" * ", "** ", " * ", " * ", " * ", " * ", "***"],                          #One
        [" *** ", "*   *", "*  * ", "  *  ", " *   ","*    ","*****"],              #Two
        ]

try:
    digits=sys.argv[1]
    row=0
    while row < 7:
        line=""
        column=0
        while column<len(digits):
            num=int(digits[column])
            digit=Digits[num]
            line+=digit[row] + "  "
            column+=1
        print(line)
        row+=1
except IndexError as inderr:
    print("usage: bigint.py %s <%s>") % (digits, inderr)
except ValueError as err:
    print(err, "in", digits)
