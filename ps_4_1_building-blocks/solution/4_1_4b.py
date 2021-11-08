# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

4b) Problem statement: Draw a flowchart (or write psuedocode) for an algorithm that lets
the user enter N integers, and then displays the sum of the absolute 
values of all the numbers entered. The value of N should also be entered
by the user. Then write a Python program to implement it, using pre-test,
for loop.
"""

N = int(input("How many integers will you enter? "))

acc = 0

for i in range(N):
    num = int(input("Enter number: "))
    acc = acc + abs(num)

print("Sum of absolute values = ", acc)
