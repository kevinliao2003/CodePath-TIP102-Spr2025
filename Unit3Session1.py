# Standard Problem Set Version 2 - Problem 3: Remove All Adjacent Duplicate Shows
"""
U - Understand
- can the string only consist of lowercase chars?
- can the string be empty?

P - Plan
variables:
- stack

loop through string
    if stack is not empty and curr char is equal to last element in stack
        pop from stack
    add curr char to stack

stringify the stack

I - Implement
- see code below
"""

def remove_duplicate_shows(schedule):
    stack = []

    for char in schedule:
        stack.append(char)

        # check for duplicates
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return "".join(stack)

res = remove_duplicate_shows("abbaca")
assert res == "ca"
res = (remove_duplicate_shows("azxxzy"))
assert res == "ay"

# Advanced Problem Set Version 1 - Problem 1: Arrange Guest Arrival Order