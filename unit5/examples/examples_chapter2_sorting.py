# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 4

Examples, Chapter 2, Sorting
    
"""

#%% imports
import random


#%% Bubble sort
def bubble_sort(A):
    n = len(A)
    for outer in range(n-1,0,-1):
        for i in range(outer):
            if (A[i] > A[i+1]):
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                

#%% test
N = 10
mylist = []
for i in range(N):
    mylist.append(random.randint(1,1000))                
    
print ("Pre-sorted list: ", mylist)    
bubble_sort(mylist)
print ("Sorted list: ", mylist)    

#%% insertion sort

def insertion_sort(mylist):
    size = len(mylist)
    
    for outer in range(1,size):
        key = mylist[outer]
        inner = outer
        
        while inner > 0 and mylist[inner-1] > key:
            mylist[inner] = mylist[inner-1]
            inner -= 1
            
        mylist[inner] = key
        
        
        
#%% test
list1 = [12,2,34,123,1,7,19]
insertion_sort(list1)
        