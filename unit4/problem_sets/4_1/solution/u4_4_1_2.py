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
  if n == 1:
    print (">>> At base case")  
    return A[0]
  else:
    return linear_sum(A,n-1) + A[n-1]
    
    
#%% function for testing fact, using the "assert" feature.
def test_linear_sum():
    A = [3,6,4,8,7,5,2]
    assert(linear_sum(A,3)==13), "test_linear_sum functional test failed. Unexpected value"        
    assert(linear_sum(A,4)==21), "test_linear_sum functional test failed. Unexpected value"        
    assert(linear_sum(A,5)==28), "test_linear_sum functional test failed. Unexpected value"        
        
    print ("linear_sum() test: PASS")        

#%% run fact test
test_linear_sum()