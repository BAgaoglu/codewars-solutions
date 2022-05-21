# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

# My Solution

def create_phone_number(n):
    list1=[]
    list1[:0] = n

    mystring1 =''.join(map(str,list1[0:3]))
    mystring2 =''.join(map(str,list1[3:6]))
    mystring3 =''.join(map(str,list1[6:]))

    return f'({mystring1}) {mystring2}-{mystring3}'