"""
Practical Algorthns
Problem set: Unit 5, set 2.1

1) Implement the bubble sort algorithm in Python. Sample solution is available
in earlier chapters, but try do it yourself first. I would suggest writing the pseudo-code yourself first too, maybe making use of deck of cards to work through the algorithm mentally first. 

"""
#%%
import sys
import random



#%% Bubble sort
#=============================================================================
def bubble_sort(A):
    """
    Sort given list in ascending order using the bubble sort algorithm
    
    Parameters
    ----------
    A : list
        unsorted list of integers

    Returns
    -------
    None.

    """    
    n = len(A)
    for outer in range(n-1,0,-1):
        for i in range(outer):
            if (A[i] > A[i+1]):
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp



#%% insertion sort
#=============================================================================

def insertion_sort(A):
    """
    Sort given list in ascending order using the insertion sort algorithm
    

    Parameters
    ----------
    mylist : A
             unsorted list of integers        

    Returns
    -------
    None.

    """
    size = len(A)
    
    for outer in range(1,size):
        key = A[outer]
        inner = outer
        
        while inner > 0 and A[inner-1] > key:
            A[inner] = A[inner-1]
            inner -= 1
            
        A[inner] = key
        



#%% MERGE SORT
#=============================================================================

#%% Merge
def MERGE(A,start,mid,end):    
    """
    The MERGE operation used in Merge Sort

    Parameters
    ----------
    A : list
        the list on which the merge operation is called
    start : integer
        starting index of the range of array on which merge is called
    mid : integer
        middle index of the range of array in which merge is called
    end : integer
        end index of the range of array in which merge is called

    Returns
    -------
    None.

    """
    #debug message, remove when not debuggin
    #print ("_MERGE_ called with start =", start, ", mid =", mid, ", end =", end)
    
    #In python, the upper index in slice operation is exclusive 
    #That is, we go up to that index, but it is not included
    #This is why the upper slicing indices are 1 more than what you see
    #in the pseudo-code
    LEFT = A[start:mid+1] 
    RIGHT = A[mid+1:end+1]
    
    #The ideal sentinel for merge sort (ascending) is "infinity"
    #That is because every number we encounter will be less than this, 
    #so we ensure that we stop considering values from L or R when we 
    #reach this "infinity" value
    LEFT.append(sys.maxsize)
    RIGHT.append(sys.maxsize)
    
    #li keeps track of LEFT array, ri keeps track of RIGHT array
    li = 0
    ri = 0
    
    #Merge L and R arrays, picking out the smaller from each at every 
    #iteration
    #Again, note that because of Pytho-specific coding, 
    #our range is from p to r+1 (as opposed to r in the pseudo-code)
    for ti in range (start,end+1):
        if LEFT[li] <= RIGHT[ri]:
            A[ti] = LEFT[li]
            li = li + 1
        else:
            A[ti] = RIGHT[ri]
            ri = ri + 1
 

#%% MERGE-SORT
def MERGE_SORT(A, start, end):
    """
    

    Parameters
    ----------
    A : list
        list of integers to be sorted
    start : integer
        starting index of range of items to be sorted
    end : integer
        ending index of range of items to be sorted

    Returns
    -------
    None.

    """
    #debug message, remove when not debuggin
    #print("MERGE SORT called on A from start =", start," to end = ", end)
    
    if start < end:
        mid = int((start+end)/2)
        MERGE_SORT(A,start,mid)
        MERGE_SORT(A,mid+1,end)
        MERGE(A,start,mid,end)

#%% QUICK SORT
#==============================================================================

#%%  Swap convenience function
def SWAP(A, i, j):
    """
    A convenience SWAP function
    (See this for a deep dive:
    https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)


    Parameters
    ----------
    A : list
        list whose elements are to be swapped
    i,j : integers
        indices that are to be swapped

    Returns
    -------
    None.

    """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
#%% Partition function
def PARTITION(A,start,end):
    """
    The PARTITION function used by QUICK SORT
    We are using the last element as the "Pivot"

    Parameters
    ----------
    A : list
        the list being paritioned
    start : integer
        starting index of the parition range
    end : integer
        ending index of the partition range

    Returns
    -------
    integer
        the final position of the pivot, at which point the given range of the
        list has been paritioned

    """   
    
    pivot = end     #pivot index "pivot" is the last index "end"
    x = A[pivot]    #read pivot value
    lrbi = start-1  #lrbi marks the boundary between < and > pivot regions, starts at -1 (if start is 0)
    
    #recall, python range goes up to but excludes the ending index, 
    #so range(start, end) will iterate from start to end-1, as required
    for ti in range (start, end):
        #swap into the "i" (or left) region any element less then pivot
        if A[ti] <= x:
            lrbi = lrbi + 1
            SWAP(A,lrbi,ti)
        #no else branch, nothing do (except increment j)
        
    #final swapping in of pivot at its appropriate location, identified
    #by the boundary marker "i" (note this is outside the loop now)
    SWAP(A,lrbi+1,end) 
    return lrbi + 1


#%% Quick sort
def QUICK_SORT(A, start, end):
    """
    The quick sort function

    Parameters
    ----------
    A : list
        list to be sorted
    start, end : integers
                 starting and ending index of range or array to be sorted

    Returns
    -------
    None.

    """
    #print message for viewing call trace, comment when not debugging
    #print ("QUICK_SORT called on A with start = ", start, ", and end = ", end)
    
    #keep partitioning and calling the sort recursively until you get 
    #so single elements (identified by p no longer being less than r)
    if start < end:
        pivot = PARTITION(A, start, end) #A[start:end] partitioned, and the position of pivot returned
        
        #debug message
        #print (": pivot with value ", A[pivot]," placed at pivot = ", pivot)
        
        #now that pivot's position is known (and it is in the correct location)
        #recursively call PARTITION_SORT on all elements on its left, and then on its right
        #but excluse the pivot itself as it is already in its correct location
        QUICK_SORT(A,start,pivot-1)
        QUICK_SORT(A,pivot+1,end)
        
#%% TESTING
#=============================================================================        
        
#%% test bubble sort
N = 10
mylist = []
for i in range(N):
    mylist.append(random.randint(1,1000))                
    
print ("Pre-sorted list: ", mylist)    
bubble_sort(mylist)
print ("Sorted list: ", mylist)    

#%% test insertion sort
N = 10
mylist = []
for i in range(N):
    mylist.append(random.randint(1,1000))                
    
print ("Pre-sorted list: ", mylist)    
insertion_sort(mylist)
print ("Sorted list: ", mylist)    


#%% Check QUICK_SORT
A = [23, 123, 5, 100, 9, 12, 3, 0, 3, 12, 1]
print (A)        
QUICK_SORT(A,0,len(A)-1)
print (A)            


#%% Testing Merge Sort
A = [23, 123, 5, 100, 9]
print (A)
MERGE_SORT(A, 0, 4)
print (A)
