# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

Problem statement: 
1b) Write a program that prompts the user to enter their last name,
and then creates a 6 character user id based on the first three
letters of their surname (in lower case), and a 3 digit randomly generated number.
"""

import random as rand

#input
last_name = input("Please enter your last name: ")

#processing
first_three_characters = last_name[0:3]
rand_3_digits = rand.randint(100,999)
user_name = first_three_characters + str(rand_3_digits)


#output
print("user_name: ", user_name)