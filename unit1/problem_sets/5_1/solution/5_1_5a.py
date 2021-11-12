# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

5a) Find the average of marks in 3 subjects for a list of 1000 students. The student's id range from 0 to 999. 
The marks can be generated randomly. 
Implement this using both lists and dictionaries
Compare the size (of the data structures) in memory as well as performance, and comment on your findings.
"""

import random
from timeit import default_timer as timer
import sys

NSTUDENTS = 10000

# assign marks randomly
record_list = []
record_dict = {}
for i in range(NSTUDENTS):
    subj1marks = random.randint(1,100)
    subj2marks = random.randint(1,100)
    subj3marks = random.randint(1,100)
    record_list.append([subj1marks, subj2marks, subj3marks])
    record_dict[i] = [subj1marks, subj2marks, subj3marks]

# finding average from list
averages_list = []
lstart = timer()
for i in range(NSTUDENTS):
    average = round((record_list[i][0] + record_list[i][1] + record_list[i][2]) / 3, 1)
    averages_list.append(average)
lend = timer()

# find average from dict
averages_dict = []
dstart = timer()
for val in record_dict.values():
    average = round((val[0] +val[1] + val[2]) / 3, 1)
    averages_dict.append(average)
dend = timer()

# compare times and sizes
print("time taken to average using list = ", lend - lstart)
print("time taken to average using dict = ", dend - lend)

print("memory used by list ds = ", sys.getsizeof(record_list))
print("memory used by dict ds = ", sys.getsizeof(record_dict))