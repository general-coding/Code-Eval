'''
Created on May 30, 2015

@author: puneeth

SUM OF INTEGERS FROM FILE
CHALLENGE DESCRIPTION:


Print out the sum of integers read from a file.

INPUT SAMPLE:

The first argument to the program will be a path to a filename containing a positive integer, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print out the sum of all the integers read from the file. E.g.

17
'''

test_case = open('input.txt')

total = 0
for test in test_case:
    total = total + int(test)
    
print(total)