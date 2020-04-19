#!/usr/bin/python

def gnomesort(lst):
    i=0
    while i < len(lst):
        if i==0 or lst[i-1]<lst[i]:
            i+=1
        else:
            lst[i-1],lst[i]=lst[i],lst[i-1]
            i-=1
    return lst

#main call
print "0(n) %s:" % gnomesort([6,5,4,3,2])
