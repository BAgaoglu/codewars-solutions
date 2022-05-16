# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

# My Solution

def abbrev_name(name):
    
    x = name.split(" ")
    return(f'{x[0][:1].upper()}.{x[1][:1].upper()}')