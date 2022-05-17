# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

# My Solution

def century(year):
     #creating a list 
    digit_string = str(year)
    digit_map = map(int, digit_string)
    year_list = list(digit_map)
    
    if len(year_list) == 2: #for 2 digits
        return 1
    
    if len(year_list) == 3: #for 3 digits
        if year_list[2] == 0 and year_list[1] == 0:
            return year_list[0]
        else:
            return year_list[0] + 1
        
    if len(year_list) == 4: #and for 4 digits
        if year_list[2] == 0 and year_list[3] == 0:
            return year_list[0]*10 + year_list[1]
        else:
            return year_list[0]*10 + year_list[1]+1