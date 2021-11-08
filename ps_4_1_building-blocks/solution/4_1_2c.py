# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building block

Problem statement: 
2c) [Multiple-alternative conditions] Draw/write the flowchart or pseudocode, 
and then write a Python program that prompts the user for a number between 1 and 12, 
corresponding to the season of the month, and then returns the season for that month,
as per the following:

Nov, Dec, Jan and Feb: Winter
Mar and Apr: Spring
May, Jun, Jul and Aug: Summer
Sep and Oct: Autumn
"""

month = int(input("Enter the month of the year (1-12): " ))

if month > 10 and month < 3:
    season = "Winter"
elif month > 2 and month < 5:
    season = "Spring"
elif month > 4 and month < 9:
    season = "Summer"
else:
    season = "Autumn"

print("The season is: ", season)    


