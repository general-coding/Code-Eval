'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj

FIBONACCI SERIES

CHALLENGE DESCRIPTION:

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1. Given an integer n>=0, print out the F(n).

INPUT SAMPLE:
The first argument will be a path to a filename containing integer numbers, one per line. E.g.

5
12

OUTPUT SAMPLE:
Print to stdout, the fibonacci number, F(n). E.g.

5
144
'''

import sys

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    print(fibo(int(test)))

test_cases.close()