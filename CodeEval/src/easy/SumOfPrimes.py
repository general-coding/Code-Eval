'''
Created on Jan 23, 2015

@author: Puneeth U Bharadwaj

SUM OF PRIMES

CHALLENGE DESCRIPTION:
Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the sum of the first 1000 prime numbers.

3682913
'''

def is_prime(num):
    for j in range(2, num):
        if (num % j) == 0:
            return False
    return True

i = 2
count = 0
sum = 0

while (count < 1000):
    if is_prime(i):
        sum = sum + i
        count = count + 1
    i = i + 1

print(sum)
