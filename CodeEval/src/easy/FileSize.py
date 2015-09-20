'''
Created on Jul 11, 2015

@author: puneeth

CHALLENGE DESCRIPTION:

Print the size of a file in bytes.

INPUT:
The first argument to your program has the path to the file you need to check the size of.

OUPUT:
55
'''

import os, sys

path = input()
print(os.path.getsize(sys.argv[1]))