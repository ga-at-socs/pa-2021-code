# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 2, set 2.1

Problem statement: 
4) Implement this "Array-Max" function in Python. Then, perform an empirical experiment where you:
i) Run the experiment for the following values of n: [10, 100, 1000, 10000]
ii) At each value of n, you run the experiment 10 times, and take the average time of these 10 runs.
You should initialize the array with random values between 1 and 1000,000 for each run.
Don't include the time to initialize the array in your experiment.
"""
import random
from timeit import default_timer as timer

RUNSPERN = 10

"""
The Array-Max function
"""
def array_max(A):
    max = A[0]
    for i in range (1,len(A)):
        if A[i] > max:
            max = A[i]



"""
main
"""

# dictionary to store results for different N's
time_results_all = {}

for N in [10, 100, 1000, 10_000, 100_000, 1000_000, 10_000_000]:
    mylist = []

    ## initialize with random integers
    for i in range(N):
        mylist.append(random.randint(1,1000_000))

    ## find max; run this 10 times, and record times
    run_times_acc = 0
    for i in range(RUNSPERN):
        start = timer()
        array_max(mylist)
        end = timer()
        run_times_acc += end-start

    average_run_time = run_times_acc / RUNSPERN 
    time_results_all[N] = average_run_time
    print(N, average_run_time)


