# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Working with Data Structures
"""

def reverse_names():
    """
    Ask  user to input 5 names, and print them in reverse order.
    Use a list and for loop
  
    Parameters
    ----------
    None

    Returns
    -------
    None.
    """

    names = []
    for i in range(5):
        names.append(input("enter a name: "))
    
    for i in range(1,6):
        print(names[-i])

reverse_names()