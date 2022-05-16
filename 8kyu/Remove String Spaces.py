# Simple, remove the spaces from the string, then return the resultant string.

# My Solution

def no_space(x):
    list1=[]
    list1[:0] = x
    word = ''

    for i in list1:
        if i == ' ':
            continue
        else:
            word+=i
    return word