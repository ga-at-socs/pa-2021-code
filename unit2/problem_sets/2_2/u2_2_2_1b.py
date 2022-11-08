# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 2, set 2.1
Implement the above algorithm in Python, and measure the time taken to sort
lists of size 10, 100, and 1000. The lists should initially be populated randomly 
with positive integers in the range 0-1000. Compare your empirical observations with 
the big-Oh complexity analysis you did in 1a)
"""

def bubble_sort(A):
    n = len(A)
    for outer in range(n-1,0,-1):
        for i in range(outer):
            if (A[i] > A[i+1]):
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp



#main
import random
from timeit import default_timer as timer

#N = 10
for N in [10,100,1000,10_000, 20_000]:
    mylist = []
    for i in range(N):
        mylist.append(random.randint(1,1000))

    start = timer()
    bubble_sort(mylist)
    end = timer()
    print(N, end-start)
