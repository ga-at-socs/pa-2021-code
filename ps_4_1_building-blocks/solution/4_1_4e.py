# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

4e) Using a post-test loop write a program that asks the user
to keep entering positive integers until their sum exceeds 
1000
"""

acc = 0

while(True):
    val = float(input("Enter value: "))
    acc = acc+val
    if (acc>1000):
        break