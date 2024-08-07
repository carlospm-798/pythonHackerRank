# Carlos Paredes Márquez
# August 7th, 2024
# Write a function that say if a year has a leap day
# leap day conditions: 
# The year can be divided by 4, is leap unless: 
#   The year can be divided by 100, not leap, unless: 
#       The year is also divisible by 400

def is_leap(year):
    leap = False
    
    if (year%4 == 0):
        leap = True
        if (year%100 == 0 and year%400 == 0):
            leap = True
        elif (year%100 == 0 and year%400 != 0):
            leap = False
    
    return leap

year = int(input())
print(is_leap(year))