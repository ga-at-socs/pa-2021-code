# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

2a) Write a python program that asks the user to enter ten integers,
and displays a list containing their squares.
"""
N = 10
squares = []

for i in range(N):
    num = input("Enter a number: ")
    squares.append(int(num)**2)

print(squares)