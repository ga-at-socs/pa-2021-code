# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building blocks

Problem statement: 
1a) Write a Python program that prompts for two inputs: the before tax price of an item, 
and the discount offered on it (as a percentage). The program should then calculate and 
display the new price, given that the sales tax rate is 17.5%.
"""

#input
before_tax = int(input("Enter the before tax price: "))
discount = int(input("Enter the discount as a percentage (1-100):"))

#processing
TAX_RATE = 0.175
price_with_tax = before_tax + (before_tax * TAX_RATE)
price_after_discount = price_with_tax - (price_with_tax * (discount/100))

#output
print("The final price after tax is: ", price_with_tax, " and with discount is: ", price_after_discount)