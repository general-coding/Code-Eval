'''
Created on Jan 21, 2015

@author: Puneeth U Bharadwaj

PRIME PALINDROME

Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the largest prime palindrome less than 1000.

929
'''

pali = []
def is_prime(num):
    for j in range(2, num):
        if (num%j)==0:
            return False
    return True

def is_palindrome(num):
    if num[::-1]==num:
        return True
    else:
        return False

for i in range(2,1001):
    if is_prime(i):
#         print i
        num = str(i)
        if is_palindrome(num):
#             print i
            pali.append(num)
            
print (max(pali))