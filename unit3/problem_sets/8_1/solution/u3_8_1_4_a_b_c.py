# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.2

Problem statement: 
    
4) Using set data structures in Python for greater good

4a)  Using sets in Python, create and test a function "count_unique()" that 
    counts the number of unique elements in a given list.
E.g. if you test it with  L = [1, 2, 3, 1, 1, 4, 5, 6], it should return: 6

4b) Using set operations in Python, create and then test a function 
    "absent_alphabets()" which, when passed a string with small-caps 
    English alphabets and whitespaces only, returns a list of the alphabets 
    that are missing in that list. So e.g.
absent_alphabets("A quick brown yes quick brown fox oh that quick brown 
fox jumps over the lazy cat") should return the list ['d', 'g']

4c) Create a function "order_neutral_list_comparison()" that accepts two 
lists as arguments, and returns True if they both have the same unique 
elements, irrespective of their order. So e.g. 
order_neutral_list_comparison([1,3,5,7,9], [1,5,7,9,9,3]) should return True
"""

#%% 4a

def count_unique(list1):
    return(len(set(list1)))

L = [1, 2, 3, 1, 1, 4, 5, 6]
print(count_unique(L))

#%% 4b

import string


def absent_alphabets(string1):
    #reduce string to unique characters
    unique_chars = set(string1.lower())
        
    absentees = []
    
    #check each letter of the alphabet to see if present in the set of 
    #unique characters derived from the input string
    for c in string.ascii_lowercase:
        if(not c in unique_chars):
            absentees.append(c)

    return (absentees)


print(absent_alphabets("A quick brown yes quick brown fox oh that quick brown fox jumps over the lazy cat"))

#%% 4c

def order_neutral_list_comparison(list1, list2):
    return(set(list1) == set(list2))
    
print(order_neutral_list_comparison([1,3,5,7,9], [1,5,7,9,9,3]))
