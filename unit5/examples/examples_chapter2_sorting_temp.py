# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:10:06 2021

@author: waqar
"""

"""
INSERTION-SORT(A)
	for outer from 1 to n-1:
	    key = A[outer]
		 inner = outer-1
		 while(key < A[inner-1) and inner > 0)
			shift A[inner-1] to A[inner]
       A[inner] = key
"""
#%%
def insertion_sort(A):
    n = len(A)
    
    for outer in range(1,n):
        key = A[outer]
        inner = outer
        
        while key < A[inner-1] and inner > 0:
            A[inner] = A[inner-1]
            inner -=1
        
        A[inner] = key
        
#%% test
list1 = [12,2,34,123,1,7,19]
insertion_sort(list1)
        