# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

2f)  Write a function join which, given two lists, it returns a list in which each element 
is a list of two elements, one from each of the given lists. For example:
join( [1,2,3] , ["a","b","c"] )
returns:           [ [1, "a"], [2, "b"], [3, "c"] ]

We assume that the given lists both have the same length.

2g) Write split, reverse of the above
"""

"""
merge_lists(list1, list2)
"""
def merge_lists(list1, list2):
    imax = len(list1)   
    olist = []
    for i in range(imax):
        olist.append([])
        olist[i].append(list1[i])
        olist[i].append(list2[i])
    return(olist)


"""
split_list (ilist)
"""
def split_list(ilist):
    imax = len(ilist)   
    list1 = []
    list2 = []
    for i in range(imax):
        list1.append(ilist[i][0])
        list2.append(ilist[i][1])

    return(list1,list2)


"""
main
"""

# create input lists
list1 = [1,2,3,5]
list2 = ["a","b","c","falanafalana"]
print("Initial lists:")
print(list1)
print(list2)

#merge lists
olist = merge_lists(list1, list2)
print("Merged list:")
print(olist)

# split_list agaibn
print("List split up again:")
newlist1, newlist2 = split_list(olist)
print(newlist1)
print(newlist2)
