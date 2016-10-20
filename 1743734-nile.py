'''
Università di Roma - Sapienza
Author: Fernando Crema
Course: Fundamentals of Data Science
HW #1: Introduction to python, pandas and numpy.
'''
from pandas import read_csv
from numpy import mean
import sys

# Read both years. Detect python version.
if (sys.version_info > (3, 0)):
    start = int(input('Give me the starting year: '))
    end = int(input('Give me the ending year: '))
else:
    start = int(raw_input('Give me the starting year: '))
    end = int(raw_input('Give me the ending year: '))

# Read Nile.csv into Data Frame
data = read_csv('Nile.csv')

# Return mean
print(mean(data[(data.time>=start) & (data.time<=end)].Nile))

