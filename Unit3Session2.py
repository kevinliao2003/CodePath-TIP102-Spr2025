# Advanced Problem Set Version 1 - Problem 4: Dream Building Layout
def min_swaps(s):
    """
    U - Understand
    - string contains only '[' and ']'
    - string can be empty

    P - Plan
    variables:
    - res (min number of swaps)
    - num_balnaced (balanced pair of walls)
        -1 for ']'
        +1 for '['

    loop over string
        if ']'
            increment num_balanced
        if '['
            decrement num_balanced
        
        update res

    return (res + 1) // 2

    I - Implement
    - see code below.
    """

    res = num_balanced = 0
    for char in s:
        if char == ']':
            num_balanced += 1
        else:
            num_balanced -= 1

        res = max(res, num_balanced)

    return (res + 1) // 2

res = min_swaps("][][")
# print(res)
assert res == 1
res = min_swaps("]]][[[")
assert res == 2
res = min_swaps("[]")
assert res == 0

# Advanced Problem Set Version 1 - Problem 5: Designing a Balanced Room
def make_balanced_room(s):
    """
    U - Understand
    - string consists of '(', ')' and lowercase English letters
    - remove the minimum number of walls
    - return any valid layout

    P - Plan
    variables:
    - stack

    convert string to a char list

    loop through string
        if open paren
            append the index to the stack
        if closed paren
            if stack is empty
                pop from the stack

            set the current char to ''

    while stack
        set the popped index to ''

    stringify s and return it

    I - Implement
    - see code below
    """

    # open = closed = 0
    # res = []
    # for char in s:
    #     if char == '(':
    #         open += 1
    #     elif char == ')':
    #         closed += 1

    #     if open < closed:
    #         closed = 0 # reset number of closed paren
    #     if char.isalpha() or open >= closed:
    #         res.append(char)

    # # edge case: there is a '(' at the end
    # if res[-1] == '(':
    #     res.pop()
    # return "".join(res)

    stack = []
    s = list(s)

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else: # unbalanced paren
                s[i] = ''

    while stack:
        popped = stack.pop()
        s[popped] = ''

    return ''.join(s)

res = make_balanced_room("art(t(d)e)sign)")
# print(res)
assert res == "art(t(d)e)sign"
res = make_balanced_room("d)e(s)ign")
# print(res)
assert res == "de(s)ign"
res = "))(("
print(res)
assert res == ""