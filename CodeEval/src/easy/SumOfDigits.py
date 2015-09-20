'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj

SUM OF DIGITS

CHALLENGE DESCRIPTION:
Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:
The first argument will be a path to a filename containing positive integers, one per line. E.g.
23
496

OUTPUT SAMPLE:
Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.
5
19
'''

import sys

test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    count = 0
    i = 0
    while i<len(test):
        if test[i] in ['1','2','3','4','5','6','7','8','9','0']:            
            count = count + int(test[i].strip())            
        i = i + 1
    
    print (count)

test_cases.close()