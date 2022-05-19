# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# monkey solution for a monkey like me
def zero(op = ''):
    if op:
        if op[1] == '*':
            return 0 * op[0]
        if op[1] == '-':
            return 0 - op[0]
        if op[1] == '+':
            return 0 + op[0]
        if op[1] == '/':
            return 0 // op[0]
    else:
        return 0
def one(op = ''):
    if op:
        if op[1] == '*':
            return 1 * op[0]
        if op[1] == '-':
            return 1 - op[0]
        if op[1] == '+':
            return 1 + op[0]
        if op[1] == '/':
            return 1 // op[0]
    else:
        return 1
def two(op = ''):
    if op:
        if op[1] == '*':
            return 2 * op[0]
        if op[1] == '-':
            return 2 - op[0]
        if op[1] == '+':
            return 2 + op[0]
        if op[1] == '/':
            return 2 // op[0]
    else:
        return 2
def three(op = ''):
    if op:
        if op[1] == '*':
            return 3 * op[0]
        if op[1] == '-':
            return 3 - op[0]
        if op[1] == '+':
            return 3 + op[0]
        if op[1] == '/':
            return 3 // op[0]
    else:
        return 3
def four(op = ''):
    if op:
        if op[1] == '*':
            return 4 * op[0]
        if op[1] == '-':
            return 4 - op[0]
        if op[1] == '+':
            return 4 + op[0]
        if op[1] == '/':
            return 4 // op[0]
    else:
        return 4
def five(op = ''):
    if op:        
        if op[1] == '*':
            return 5 * op[0]
        if op[1] == '-':
            return 5 - op[0]
        if op[1] == '+':
            return 5 + op[0]
        if op[1] == '/':
            return 5 // op[0]
    else:
        return 5
def six(op = ''):
    if op:
        if op[1] == '*':
            return 6 * op[0]
        if op[1] == '-':
            return 6 - op[0]
        if op[1] == '+':
            return 6 + op[0]
        if op[1] == '/':
            return 6 // op[0]
    else:
        return 6
    
def seven(op = ''):
    if op:
        if op[1] == '*':
            return 7 * op[0]
        if op[1] == '-':
            return 7 - op[0]
        if op[1] == '+':
            return 7 + op[0]
        if op[1] == '/':
            return 7 // op[0]
    else:
        return 7
    
def eight(op = ''):
    if op:
        if op[1] == '*':
            return 8 * op[0]
        if op[1] == '-':
            return 8 - op[0]
        if op[1] == '+':
            return 8 + op[0]
        if op[1] == '/':
            return 8 // op[0]
    else:
        return 8
def nine(op = ''):
    if op:
        if op[1] == '*':
            return 9 * op[0]
        if op[1] == '-':
            return 9 - op[0]
        if op[1] == '+':
            return 9 + op[0]
        if op[1] == '/':
            return 9 // op[0]
    else:
        return 9

def plus(num2):
    list1 = [num2, '+']
    return list1
def minus(num2):
    list1 = [num2, '-']
    return list1
        
def times(num2): 
    list1 = [num2, '*']
    return list1

def divided_by(num2):
    list1 = [num2, '/']
    return list1