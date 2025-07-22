#!/usr/bin/python
number=100
print '\n'.join(['fizz'*(not n%3)+'buzz'*(not n%5) or str(n) for n in range(1,number)])
