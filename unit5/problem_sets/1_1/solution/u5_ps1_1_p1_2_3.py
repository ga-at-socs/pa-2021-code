# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 5, 1.1

Problem statement: 

1. Without referring to the code available in the previous chapter, write a 
sequential search algorithm that searches for an integer in a given list of 
integers. Assume input list is not sorted.

2. Without referring to the code available in the previous chapter, 
write a sequential search algorithm that searches for an integer in a given 
list of integers. Assume input list is sorted (so your search function should 
exit as soon as it finds a value greater than the one you are looking for).

3. Without referring to the code available in the previous chapter, 
Implement the binary search algorithm that finds a given integer 
in a sorted list of integers. 

"""

#%% sequential search
def sequential_search(list1, val):
    """
    Carry out a sequential search of the given list for a given value
    
    Parameters
    ----------
    list1: input list, no prior sorting assumed
    val: the value to be searched

    Returns
    -------
    True/False
    """

    for i in range(len(list1)):
        if list1[i] == val:
            return True
    return False

#%% test sequential_search
mylist = [1,2,3,4,15,20,25,100]
assert (sequential_search(mylist, 10)==False)
assert (sequential_search(mylist, 4)==True)
print("Sequential search test passed")

#%% sequential search, ordered input
def sequential_search_ordered_input(list1, val):
    """
    Carry out a sequential search of the given sorted list for a given value
    
    Parameters
    ----------
    list1: input list, assumed to be sorted in ascending order
    val: the value to be searched

    Returns
    -------
    True/False
    """
    for i in range(len(list1)):
        #found the value of interest; return
        if list1[i] == val:
            return True
        #found a value greater than the value of interest. Since the list
        #is sorted and the value of interest hasn't been found, it must not be
        #present, return with false
        if list1[i] > val:
            return False
    return False

#%% test
mylist = [1,2,3,4,15,20,25,100]
assert (sequential_search_ordered_input(mylist, 10)==False)
assert (sequential_search_ordered_input(mylist, 4)==True)
print("Sequential search (ordered list) test passed")

#%% Binary search
def binary_search(list1, val):
    """
    Carry out binary search of the given sorted list for a given value
    
    1 Look at the middle value; then
    
    2 If the middle item is the search item, or no more elements left, exit.
     
    3 if search item is greater than the value at the middle, 
        it must be on its right. Discard middle item and left half. 
        Repeat 1
    4 if search item is less than the value at the middle, 
        it must be on its left. Discard the middle item and right half. 
        Repeat 1
    
    Parameters
    ----------
    list1: input list, sorted
    val: the value to be searched

    Returns
    -------
    True/False
    """

    size = len(list1)
    mid = size // 2
    
    #debug message, remove when not debugging
    print ("Binary search called on this list: ", list1, " of size ", size)
    
    #base case
    if size == 0:
        return False
    
    #item found
    if(list1[mid]==val):
        return True
    
    #recursive call
    if(list1[mid] < val):
        return binary_search(list1[mid+1:size],val)
    else:
        return binary_search(list1[0:mid],val)
    
#%% test binary search 
mylist = [1,2,3,4,15,17,19,20,21,25,28,100,120]
assert (binary_search(mylist, 10)==False)
assert (binary_search(mylist, 100)==True)
print("Sequential search (ordered list) test passed")
