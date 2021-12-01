# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.1

Problem statement: 

2. Write the LINEAR_SUM function from the lecture slides in chapter 4. 
Draw its call graph for n = 3 and A = {3,6,4,8,7,5,2}, and then test it 
in your program with the same values. 
Use print messages to display its call trace.
"""


#%% The recursive factorial function
def linear_sum(A,n):
  print ("linear_sum called with n = ", n)
<YOUR-CODE-HERE>    
    
    
#%% function for testing fact, using the "assert" feature.
def test_linear_sum():
    A = [3,6,4,8,7,5,2]
<YOUR-CODE-HERE>    
        
    print ("linear_sum() test: PASS")        

#%% run fact test
test_linear_sum()