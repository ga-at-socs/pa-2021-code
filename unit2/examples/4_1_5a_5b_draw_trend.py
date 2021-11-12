# -*- coding: utf-8 -*-
"""
Practical Algorithms Example
Topic: Unit 2, Algorithmic Analysis

Problem statement: 

a) Write a Python program using a for loop that sums up the first n
integers. Use a timer function to record how long it takes. 

b) Now write the same program, but this time use a while loop. 
How long does this this version take?

c) repeat the problem, using the summation formula n(n+1)/2

Repeat the above experiment for a number of different n's and record results
in a dictionary.
Export as a CSV file
"""

#%% output to CSV files?
OUT2CSV = None

#%% dependencies

from timeit import default_timer as timer
import csv

# dictionary to store the results
results = {"A": {}, "B": {}, "C": {} }

for n in range(1_000_000 , 11_000_000, 1_000_000):
    #%% Version A of the solution
    acc = 0

    start = timer()
    for i in range(n+1):
        acc = acc + i
    end  = timer()
    walltime = end-start
    print ("n = ", n, " :: result ver A = ", acc, " :: execution time ver A =  ", walltime)
    results["A"][n] = walltime


    #%% Version B of the solution
    acc = 0
    i = 0

    start = timer()
    while i < n+1:
        acc = acc + i
        i = i+1
    end  = timer()
    walltime = end-start
    print ("n = ", n, " :: result ver B = ", acc, " :: execution time ver B =  ", walltime)
    results["B"][n] = walltime


    #%% Version C of the solution
    acc = 0
    start = timer()
    acc = (n * (n+1))/2
    end  = timer()
    walltime = end-start
    print ("n = ", n, " :: result ver C = ", acc, " :: execution time ver C =  ", walltime)
    results["C"][n] = walltime

# %% Write results to CSV files

if(OUT2CSV):
    with open('resultsA.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, results["A"].keys())
        w.writeheader()
        w.writerow(results["A"])

    with open('resultsB.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, results["B"].keys())
        w.writeheader()
        w.writerow(results["B"])    

    with open('resultsC.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, results["C"].keys())
        w.writeheader()
        w.writerow(results["C"])