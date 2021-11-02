# -*- coding: utf-8 -*-
"""
Practical Algorthns
problem set: building blocks
problem: timing loops

This is the  incomplete version for you to try to complete on your own
Look for the tag <YOUR_CODE_HERE> to see where to put your code
Try your best to do it yourself before looking at the solution

If you are doing this from scratch, your solution may look different,
which is fine as well...
"""

#%% dependencies

from timeit import default_timer as timer
#%% problem size
n = 20000000

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
