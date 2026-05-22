import sys

def split_int(num,parts):
    quotient,rem_parts=divmod(num,parts)
    upper=[quotient + 1 for i in range(rem_parts)]
    lower=[quotient for i in range(parts-rem_parts)]
    return lower + upper

num=int(sys.argv[1])
parts=int(sys.argv[2])
print split_int(num,parts)
