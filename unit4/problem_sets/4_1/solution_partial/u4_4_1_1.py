# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.1

Problem statement: 

1a. Write the fact (factorial) function in Python. 
Draw its call trace with pen and paper for fact(5). 
The call trace should show the sequence of calls as well as the return values 
from each call (see lecture slides for example). 
Use print messages to display its call trace 
(e.g., "I am inside the  fact() function, with n = ...").     

1b. Is FACT a tail recursive function? Justify your answer.

1c. Is FACT a linear recursive function? Justify your answer.
"""


#%% The recursive factorial function
def fact(n):
    print ("FACT called with n = ", n)
    if n == 1:
<YOUR-CODE-HERE>    
    
#%% function for testing fact, using the "assert" feature.
def test_fact():
    assert(fact(5)==120), "FACT functional test failed. Unexpected value"        
    assert(fact(8)==40320), "FACT functional test failed. Unexpected value"        
    assert(fact(10)==3628800), "FACT functional test failed. Unexpected value"        
        
    print ("fact() test: PASS")        

#%% run fact test
test_fact()