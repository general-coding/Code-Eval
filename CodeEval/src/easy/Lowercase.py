'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj

LOWERCASE

CHALLENGE DESCRIPTION:
Given a string write a program to convert it into lowercase.

INPUT SAMPLE:
The first argument will be a path to a filename containing sentences, one per line.
You can assume all characters are from the english language. E.g.

HELLO CODEEVAL
This is some text

OUTPUT SAMPLE:
Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

hello codeeval
this is some text
'''

import sys

test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    lowerstr = test.lower()
    print (lowerstr)
    lowerstr = ' '

test_cases.close()