# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

2e) Write a Python program that let's the user enter 20 integers, 
organized as a 4x5 matrix (implemented as a 2D list),
and then "truncates" all values that are negative (that is, replaces all negative values with a zero).
The resulting matrix is then displayed on the screen
"""

NROWS = 4
NCOLS = 5

datamat = []

for i in range(NROWS):
    datamat.append([])
    for j in range(NCOLS):
        #datamat[i].append(int(input("Enter number at row = ", i, " and col = ", j)))
        prompt = "Enter number at row = " + str(i) + " and col = " + str(j) + " : "
        datamat[i].append(int(input(prompt)))
        if(datamat[i][j] < 0):
            datamat[i][j] = 0


for row in datamat:
    print(row)



