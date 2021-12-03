# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 4

Examples, Chapter 1, Searching
    
"""

10 in [1,2,3,4,15,20,25,100]
4 in [1,2,3,4,15,20,25,100]


#%% sequential search
def sequential_search(list1, val):
    for i in range(len(list1)):
        if list1[i] == val:
            return True
    return False

#%% test
mylist = [1,2,3,4,15,20,25,100]
sequential_search(mylist, 10)
sequential_search(mylist, 4)

#%% sequential search
def sequential_search_ordered_input(list1, val):
    for i in range(len(list1)):
        if list1[i] == val:
            return True
        if list1[i] > val:
            return False
    return False

#%% test
mylist = [1,2,3,4,15,20,25,100]
sequential_search_ordered_input(mylist, 10)
sequential_search_ordered_input(mylist, 4)

#%% Binary search
"""
1 Look at the middle value; then

2 If the middle item is the search item, or no more elements left, exit.
 
3 if search item is greater than the value at the middle, 
    it must be on its right. Discard middle item and left half. 
    Repeat 1
4 if search item is less than the value at the middle, 
    it must be on its left. Discard the middle item and right half. 
    Repeat 1

"""

def binary_search(list1, val):
    size = len(list1)
    mid = size // 2
    
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
binary_search(mylist,100)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
























