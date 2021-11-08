# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

4c) Write a Python program that prompts the user to enter 
numeric values repeatedly until the value 0 is entered. 
It then displays the
mean of the values entered. Use the pre-test while loop. 
(Note that in addition to the pre-test, you \ewill also need a
 "mid-test" in the loop).
"""

val = float(input("Enter value: "))

acc = 0
count = 0

while val != 0:
    acc = acc+val
    count = count + 1
    val = float(input("Enter value: "))

mean = acc / count
print ("mean = ", mean)