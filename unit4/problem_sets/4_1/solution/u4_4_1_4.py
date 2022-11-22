# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.1

Problem statement: 

4. You will note that the version of FACT in 1 is not tail-recursive. 
That is because the recursive call is not last operation in the fact function; 
there is a multiplication operation that happens after the recursive call 
(that is, on the way back).

It is possible to convert this function into a tail-recursive function 
fact_tail, by passing it an accumulator parameter along with the parameter n,
and performing the multiplication on the way down.

4a) See if you can write this pseudo-code for fact_tail on your own first. 
    If you get stuck, look it up at the bottom of this page.

4b) Now implement the fact_tail function in Python.
    
4c) Implement in Python, an iterative version of fact_tail.
    
4d) What is the complexity of fact_iter?
    
"""


#%% generic function for testing FACT
# We are defining a _generic_ fact tester; that is, we can pass this tester
# the name of the function we want tested. This lets us use the same tester
# for different versions of our factorial function
    
def test_fact(func2test):    
    assert(func2test(5)==120), "FACT functional test failed. Unexpected value"        
    assert(func2test(8)==40320), "FACT functional test failed. Unexpected value"        
    assert(func2test(10)==3628800), "FACT functional test failed. Unexpected value"        
        
    print ("function test: PASS")        


#%% 4a and 4b
# *TAIL* Recusrice Factorial Function
# We are not allowed to peform operations on the return path
# So what we peform the multiplication and accumulation on the _downward_
# path throught the recursion tree.
# We pass an accumulator initialized at 1 to the first recursive call for "n"
# It multiplies n with the accumulator, and then recursively calls function for
# n-1 while also passing it the accumulator.
# We keep doing this until we get to the base case, at which point we have 
# our answer; no computations now needed on the return path


# we pass acc a default value of 1, for the first call to fact_tail which 
# which requires acc to be initialized to 1
def fact_tail(n, acc=1):
    #print ("FACT called with N = ", N)
    if n == 1:
        return acc
    else: 
        acc = n * acc
        return fact_tail(n-1, acc)


#run test
test_fact(fact_tail)


#%% 4c

def fact_iter(n):
    acc = 1
    while n > 1:
        acc = n * acc
        n = n-1
    return acc

# run test
test_fact(fact_iter)

#%% 4d

"""
fact_iter loops n times (starts at n, goes down to 1, decrementing by 1 at
each step). So its complexity is O(n)
"""
    

