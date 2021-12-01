# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.1

Problem statement: 

3. Write the (tail) recursive as well as the iterative version of 
the "reverse array" function discussed in class. 
The pseudo-codes are shown below.  
Use print messages to display the call trace of the recursive version.
"""


#%% REVERSE ARRAY
def reverse_array(A,i,j):
    print ("reverse_array called with i = ", i, " j = ", j)
<YOUR-CODE-HERE>    
    
    
#%% function for testing fact, using the "assert" feature.
def test_reverse_array():
    A = [3,6,4,8,7,5,2]
    reverse_array(A,0,len(A)-1) #note that reverse_array changes A in-place
    assert(A==[2,5,7,8,4,6,3]), "reverse_array functional test failed. Unexpected value"        
        
    print ("reverse_array() test: PASS")        

#%% run test_reverse_array
test_reverse_array()
