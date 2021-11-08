# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building block

Problem statement: 
[Single-alternative condition] Draw/write the flowchart or pseudocode, 
and then write a Python program that asks the user to input two numbers,
and tells you if one is a multiple of the other 
(so, e.g., if you enter 18 and 6, or 6 and 18, it should return "True". If not, nothing displayed*). 
"""

n1 = int(input("Enter first number: " ))
n2 = int(input("Enter second number: "))


#since the numbers could be entered in any order (not necessarily bigger number first)
#so we check for both (is first number multiple of second, or is second number multiple of first)
if n1 % n2 == 0 or n2 % n1 == 0:
    print("True: One of the numbers you entered is a multiple of the other")