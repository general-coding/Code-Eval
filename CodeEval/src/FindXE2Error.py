'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj
'''

with open("FibonacciSeries.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print(i, repr(line))