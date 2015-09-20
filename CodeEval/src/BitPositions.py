'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj

BIT POSITIONS

CHALLENGE DESCRIPTION:
Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not.
Positions p1 and p2 are 1 based.

INPUT SAMPLE:
The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line. E.g.

1 86,2,3
2 125,1,2

OUTPUT SAMPLE:
Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.
1 true
2 false
'''

xynlist = []
a = 0
b = 0
test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    xynlist = test.split(',')
    n = int(xynlist[0])
    p1 = int(xynlist[1])
    p2 = int(xynlist[2])
    bit = bin(n)[2:]
    
    if p1 > len(bit) or p2 > len(bit):
            bit = '0' * (max(p1, p2) - len(bit)) + bit
            print bit
            
    print('true' if bit[-p1] == bit[-p2] else 'false')
    
test_cases.close()