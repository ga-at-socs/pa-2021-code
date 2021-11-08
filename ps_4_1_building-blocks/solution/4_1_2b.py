# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building block

Problem statement: 
2b) [Dual-alternative condition] Draw/write the flowchart or pseudocode, and then write a 
Python program that prompts the user for hourly pay rate and the number of hours worked in
a given week, and returns the gross pay. The hourly rate applies for up to 40 hours of work,
and any hours worked over 40 are paid at 1.5 times the given hourly rate. 
"""

pay_rate = float(input("Enter hourly pay rate: " ))
hours = float(input("Number of hours worked: "))

if(hours < 40):
    gross_pay = hours*pay_rate
else:
    gross_pay = (40*pay_rate) + (1.5*pay_rate*(hours-40))

print ("gross pay = ", gross_pay)