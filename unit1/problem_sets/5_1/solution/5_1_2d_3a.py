# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

2d and 3a

"""

from timeit import default_timer as timer
import sys

N = 1_000_000


# 2d
"""
Create a list of a million elements, populated with the 
first million natural numbers. Using a for loop, (so no direct 
formulas or other exotic approaches like using a map*), calculate 
the sum of all the elements of the list.
"""
mylist = []
start = timer()
for i in range(N):
    mylist.append(i+1)
end = timer()
print("Time taken to create list = ", end-start)

sum = 0
start = timer()
for i in range(N):
    sum += mylist[i]
end = timer()
print("Time taken to compute sum = ", end-start)

print("sum = ", sum)

print("size of list = ", sys.getsizeof(mylist), "\n\n")


# 3a
"""
Repeat problem 2d, using arrays instead of lists
"""
import array as arr


myarray = arr.array('i', [0] * N)
start = timer()
for i in range(N):
    myarray[i] = i+1
end = timer()
print("Time taken to create array  = ", end-start)

sum = 0
start = timer()
for i in range(N):
    sum += myarray[i]
end = timer()
print("Time taken to compute sum = ", end-start)

print("sum = ", sum)

print("size of array = ", sys.getsizeof(myarray))
