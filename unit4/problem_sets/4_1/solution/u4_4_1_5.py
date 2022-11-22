# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.1

Problem statement: 

5. Consider the algorithm described by the following pseudo-code:
See problem 5 here https://moodle.gla.ac.uk/mod/book/view.php?id=2721558&chapterid=81423

5g) Write python program that  im plements both recursive as well as the 
    iterative version of this algorithm. Test if with m = 3 and n = 4, and 
    check that the result matches your computed value in 5b.

    
"""


#%% 
"""
 5a) The function computes m^n
"""

#%% tester
def tester(fun2test):
    assert(fun2test(3,4)==81), "functional test failed. Unexpected value"        
    assert(fun2test(3,3)==27), "functional test failed. Unexpected value"        
    print ("function test: PASS")  
#%% the F function
def F(m,n):
    if n==0:
        return 1
    else:
        return (m*F(m,n-1))
    
#%%  test
tester(F)

#%% the F function
def F_iter(m,n):
    acc = 1
    while n > 0:
        acc = acc*m
        n = n-1
    return acc

#%%  test
tester(F_iter)

