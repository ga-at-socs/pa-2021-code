"""
Practical Algorthns
Problem set: Unit 5, set 2.1

Code for:
    + Merge Sort
    + Quick Sort
This is the  incomplete version for you to try to complete on your own
Look for the tag <YOUR_CODE_HERE> to see where to put your code
Try your best to do it yourself before looking at the solution
"""
#%%
import sys

#==============================================================
# MERGE SORT
#==============================================================

#%% Merge
def MERGE(A,p,q,r):
    #calculating the sizes of L and R
    #we will place our "sentinels" at this value
    n1 = <YOUR_CODE_HERE>
    n2 = <YOUR_CODE_HERE>
    
    print ("_MERGE_ called with p =", p, ", q =", q, ", r =", r, ", n1 =", n1, ", n2 =", n2)
    
    #In python, the upper index in slice operation is exclusive 
    #That is, we go up to that index, but it is not included
    #This is why the upper slicing indices are 1 more than what you see
    #in the pseudo-code
    L = A[<YOUR_CODE_HERE>] 
    R = A[<YOUR_CODE_HERE>]
    
    #The ideal sentinel for merge sort (ascending) is "infinity"
    #That is because every number we encounter will be less than this, 
    #so we ensure that we stop considering values from L or R when we 
    #reach this "infinity" value
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    
    #i keeps track of L array, j keeps track of R array
    i = 0
    j = 0
    
    #Merge L and R arrays, picking out the smaller from each at every 
    #iteration
    #Again, note that because of Pytho-specific coding, 
    #our range is from p to r+1 (as opposed to r in the pseudo-code)
    for k in range (p,r+1):
        <YOUR_CODE_HERE> 
        
#%% Test Merge
A = [1, 3, 5, 2, 3]
MERGE(A, 0, 2, 4)

#%% MERGE-SORT
def MERGE_SORT(A,p,r):
    print("MERGE SORT called on A from p =", p," to r = ", r)
    
    if <YOUR_CODE_HERE>:
        <YOUR_CODE_HERE>

#%% Testing Merge Sort
A = [23, 123, 5, 100, 9]
MERGE_SORT(A, 0, 4)
print (A)


#==============================================================
# QUICK SORT
#==============================================================

#%% A convenience SWAP function
#(See this for a deep dive: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)

def SWAP(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
#%% The PARTITION function used by QUICK SORT
# We have decided to use the last element as the "Pivot"
def PARTITION(A,p,r):
    <YOUR_CODE_HERE>     #pivot index "q" is the last index "r"
    <YOUR_CODE_HERE>  #read pivot value
    <YOUR_CODE_HERE>   #i marks the boundary between < and > pivot regions, starts at -1 (if p is 0)
    
    #recall, python range goes up to but excludes the ending index, 
    #so range(p,r) this will iterate from p to r-1, as indicated in the pseudo code
    <YOUR_CODE_HERE>
        #swap into the "i" (or left) region any element less then pivot
        <YOUR_CODE_HERE>
        #no else branch, nothing do (except increment j)
        
    #final swapping in of pivot at its appropriate location, identified
    #by the boundary marker "i" (note this is outside the loop now)
    <YOUR_CODE_HERE>

#%% Check PARTITION
# partition used just once to check its working
A = [23, 123, 5, 100, 9]
PARTITION(A,0,4)
print (A)

#%% Partition sort
def QUICK_SORT(A,p,r):
    #print message for viewing call trace
    print ("QUICK_SORT called on A with p = ", p, ", and r = ", r, end = "")
    
    #keep partitioning and calling the sort recursively until you get 
    #so single elements (identified by p no longer being less than r)
    if <YOUR_CODE_HERE>:
        q = PARTITION(A,p,r) #A[p:r] partitioned, and the position of pivot returned
        print (": pivot with value ", A[q]," placed at q = ", q)
        #now that pivot's position is known (and it is in the correct location)
        #recursively call PARTITION_SORT on all elements on its left, and then on its right
        #but excluse the pivot itself as it is already in its correct location
        <YOUR_CODE_HERE>    
    else:
        #just printing end of line
        print("")
        
#%% Check QUICK_SORT
A = [23, 123, 5, 100, 9, 12, 3, 0, 3, 12, 1]
print (A)        
QUICK_SORT(A,0,len(A)-1)
print (A)        
