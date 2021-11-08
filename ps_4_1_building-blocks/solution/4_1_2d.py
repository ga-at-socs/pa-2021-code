# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Algorithmic building block

Problem statement: 
2d) [Nested conditions] Modify the program you wrote for 2c to add another prompt
to the user which asks them: "Is this question about Scotland?". 
If they answer yes to this question, then the season should be
calculated as described here:

Jun: June
Jul to May: Winter
Otherwise, the season should be calculated as described in 2c
(you know, the way science says it is supposed to be). 
"""

month = int(input("Enter the month of the year (1-12): " ))
scotland = input("Is this question about Scotland? (yes/no): ")

if(scotland.lower() == "yes"):
    if month == 6:
        season = "June"
    else:
        season = "Winter"
else:
    if month > 10 and month < 3:
        season = "Winter"
    elif month > 2 and month < 5:
        season = "Spring"
    elif month > 4 and month < 9:
        season = "Summer"
    else:
        season = "Autumn"

print("The season is: ", season)    
