# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

Problem statement: 
3) Is the number a Palindrome?
Palindrome numbers that remain the same even when you reverse the digits. 
So e.g. 12321 is a 5-digit palindrome. 
Write a Python program that prompts the user to enter a 5-digit number, 
and checks if it is a palindrome. The program should display error messages 
if the user enters a floating point number, or a number that has less or more 
than 5 digits. This is not the problem for using exceptions, we want to use 
conditionals for checking for errors
"""

def check_palindrome(n):
    """
    Checks if the 5 digit number passed is a palindrome
  
    Parameters
    ----------
    n = input number

    Returns
    -------
    True if number if palindrome. False otherwise
    """
    if(n != int(n)):
        print("You entered a float")
        quit()
    elif n < 10000 or n > 99999:
        print("The number you entered has less or more than 5 digits")
        quit()
    else:
        n_str = str(int(n))
        if n_str[0] == n_str[-1] and n_str[1] == n_str[-2]:
            print("The number is a palindrome")
        else:
            print("The number is NOT a palindrome")


#main
num = input("Enter a 5-digit number: ")
check_palindrome(float(num))


