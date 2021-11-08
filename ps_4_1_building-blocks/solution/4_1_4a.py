# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

Problem statement:
4a) Draw a flowchart (or write psuedocode) for an algorithm that lets
the user enter N integers, and then displays the sum of the absolute 
values of all the numbers entered. The value of N should also be entered
by the user. Then write a Python program to implement it, using the pre-test,
while loop.
"""

N = int(input("How many integers will you enter? "))

i = 0
acc = 0

while i<N:
    num = int(input("Enter number: "))
    acc = acc + abs(num)
    i = i+1

print("Sum of absolute values = ", acc)
