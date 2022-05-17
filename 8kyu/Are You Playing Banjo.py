# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

# My Solution

def are_you_playing_banjo(name):
    
    list1=[]
    list1[:0] = name

    if list1[0] == 'r' or list1[0] == 'R':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'