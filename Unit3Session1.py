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
"""
U - Understand
- string can only consits of 'I' and 'D'
- string can't be empty

P - Plan
- greedy approach using a stack
variables:
- stack
- num (smallest num)
- res (answer to return)

iterate over string
    stringify num and add it to the stack
    increment num

    if i is the last index or the current char is 'I'
        pop from the stack and append the value to res

stringify res and return it

I - Implement
- see code below
"""

def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    stack, res = [], []
    num = 1 # current smallest num

    for i in range(n + 1):
        stack.append(str(num))
        num += 1

        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                res.append(stack.pop())

    # pop remaining elements
    while stack:
        res.append(stack.pop())
    return ''.join(res)

res = arrange_guest_arrival_order("IIIDIDDD")
# print(res)
assert res == "123549876"
res = arrange_guest_arrival_order("DDD")
assert res == "4321"