# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 06:50:57 2021

@author: waqar
"""

#%% recursive factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#%% use
        
res = factorial (4)
print (res)
    