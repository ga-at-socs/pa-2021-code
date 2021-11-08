# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: building blocks

Problem statement: 
We are going to do some a few small timing experiments, sneaking in some advanced
preparatory work for a key concept that we cover in this course: Algorithmic Analysis.
But let's not let these terminologies get in the way for now. We are just writing 
some code  involving loops, and measuring how long they take.

5a) Write a Python program using a for loop that sums up the first n
integers, where n = 10,000,000 (10 million). Use a timer function to record how long it takes. 

5b) Now write the same program, but this time use a while loop. 
How long does this this version take?
"""

#%% dependencies

from timeit import default_timer as timer
#%% problem size
n = 10000000

#%% Version A of the solution
acc = 0

start = timer()
for i in range(n+1):
    acc = acc + i
end  = timer()
print ("result ver A = ", acc, " :: execution time ver A =  ", end - start)


#%% Version B of the solution
acc = 0
i = 0

start = timer()
while i < n+1:
    acc = acc + i
    i = i+1
end  = timer()

print ("result ver B = ", acc, " :: execution time ver B =  ", end - start)

#%% Version C of the solution
acc = 0
start = timer()
acc = (n * (n+1))/2
end  = timer()

print ("result ver C = ", acc, " :: execution time ver C =  ", end - start)
