'''
Università di Roma - Sapienza
Author: Fernando Crema
Course: Fundamentals of Data Science
HW #1: Introduction to python, pandas and numpy.
'''
import sys

def my_prime(N):
    if N == 1:
        return 1

    if N==2 or N ==3 or N==5:
        return 'prime'

    if N % 2 == 0:
        return 2

    if N % 3 == 0:
        return 3

    if N % 5 == 0:
        return 5

    idx = 6

    while idx*idx <= N:
        if N%(idx-1) == 0:
            return idx-1
        if N%(idx+1) == 0:
            return idx+1
        idx += 6
    
    return 'prime'

# Read N. Detect python version.
if (sys.version_info > (3, 0)):
    print(my_prime(int(input('Tell me the number: '))))
else:
    print(my_prime(int(raw_input('Tell me the number: '))))
