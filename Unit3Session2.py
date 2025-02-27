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