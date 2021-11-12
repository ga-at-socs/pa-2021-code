# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

Write a python program that reads integers stored in this file,
and creates a new file containing the square of those numbers
in the same format.
"""

with open("read_data_to_list_source.txt") as fh:
    nums = fh.readlines()

squared = []    
#for i in range(len(nums)-1):
#    print(int(nums[i].strip()))

with open("squared.txt", "w") as outfh:
    for val in nums:
        if val != "\n":
            #squared.append(int(val)**2)
            outfh.write(str(int(val)**2) + "\n")
