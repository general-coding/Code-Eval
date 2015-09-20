'''
Created on Jan 24, 2015

@author: Puneeth U Bharadwaj

REVERSE WORDS

CHALLENGE DESCRIPTION:
Write a program which reverses the words in an input sentence.

INPUT SAMPLE:
The first argument is a file that contains multiple sentences, one per line.
Empty lines are also possible.

For example:
1 Hello World
2 Hello CodeEval

OUTPUT SAMPLE:
Print to stdout each sentence with the reversed words in it, one per line.
Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.

For example:
1 World Hello
2 CodeEval Hello
'''

xynlist = []
revstr = ' '
test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    xyn = str(test)
    xynlist = xyn.split()
    xynlist.reverse()
    
    for item in xynlist:
        revstr = revstr + item + ' '
    
    print (revstr.strip())
    revstr = ' '

test_cases.close()