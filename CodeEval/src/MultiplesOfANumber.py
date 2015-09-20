'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj

MULTIPLES OF A NUMBER

CHALLENGE DESCRIPTION:
Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. 
Do not use division or modulo operator.

INPUT SAMPLE:
The first argument will be a path to a filename containing a comma separated list of two integers, one list per line. E.g.
13,8
17,16

OUTPUT SAMPLE:
Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.
16
32
'''

xynlist = []
test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    xynlist = test.split(',')
    x = int(xynlist[0])
    n = int(xynlist[1])
    
    prod = 0
    i = 1
    
    while True:
        prod = n * i
        i = i + 1
        
        if prod>=x:
            break
    
    print (prod) 
    
test_cases.close()