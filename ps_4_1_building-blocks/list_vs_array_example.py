# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 

"""

def sum_10_natnums_list():
    """
    square and display first ten natural numbers using list
  
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    
    num_list = []
    for i in range(10):
        num_list.append(i)
     
    num_list_squared = []   
    for i in range(10):
        num_list_squared.append(num_list[i]**2)
        print(num_list_squared[i])
        
def sum_10_natnums_array():
    """
    square and display first ten natural numbers using list
  
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    import array as arr
    
    num_array = arr.array('i', [0] * 10)
    for i in range(10):
        num_array[i] = i
     
    num_array_squared = arr.array('i', [0] * 10)
    for i in range(10):
        num_array_squared[i] = num_array[i]**2
        print(num_array_squared[i])



sum_10_natnums_list()
sum_10_natnums_array()