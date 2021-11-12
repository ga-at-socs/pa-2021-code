# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

2c:
Write a Python program that prompts reads names from this text file, stores them in a list,
and then displays the indices of those that start with an "a". 
"""

with open("read_names_to_list_source.txt") as fh:
    names = fh.readlines()

#"enumerate" iterates through a list with 
#convenience access to both index and value
for i, name in enumerate(names):
    #check this was not a blank line
    if (name != "\n"):
        #cbeck first character, case in-sensitive
        if(name[0].lower() == 'a'):
            print (i)