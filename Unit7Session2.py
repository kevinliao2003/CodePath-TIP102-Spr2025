# Advanced Problem Set Version 1 - Problem 4: Smallest Letter Greater Than Target
def next_greatest_letter(letters, target):
    """
    U - Understand
    - the list is sorted in increasing order
    - at least 2 different characters in the list
    - if no character exists, return the 1st character
    - list is not empty?

    M - Match
    - binary search

    P - Plan
    variables
    - l (left pointer)
    - r (right pointer)

    while l <= r
        get the middle index
        if the middle index is greater than target
            set r to m
        else
            set l to m + 1

    return r

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(logn) where n is the size of letters
    - SC: O(1)
    """

    l, r = 0, len(letters) - 1
    while l < r:
        m = (l + r) // 2
        if letters[m] > target:
            r = m
        else:
            l = m + 1

    # edge case: no such character exists
    return letters[l] if l != len(letters) - 1 else letters[0]

letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']
assert next_greatest_letter(letters, 'a') == 'b'
assert next_greatest_letter(letters, 'd') == 'e'
assert next_greatest_letter(letters, 'y') == 'a'

# Advanced Problem Set Version 2 - Problem 2: Concert Ticket Search II
def find_affordable_ticket(prices, budget):
    """
    U - Understand
    - find a concert ticket closed to the target
    - prices is sorted in increasing order
    - algo must run in O(logn) time
    - price must not be greater than the budget
    - return -1 if no ticket is found

    M - Match
    - binary search

    P - Plan
    variables:
    - l (left pointer) to 0
    - r (right pointer) to last index
    - res_idx, res_num

    while l < r
        get middle index (m)
        if m is less than target and the diff is less or equal to than the diff between res_num and target
            update res_num
            update res_idx
            set r to m
        else
            set l to m + 1

    return res_idx

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    """

    l, r = 0, len(prices) - 1
    res_idx = -1 # if no ticket is found, return -1

    while l < r:
        m = (l + r) // 2
        if prices[m] == budget:
            return m
        elif prices[m] < budget:
            res_idx = m
            l = m + 1
        else:
            r = m

    return res_idx

res = find_affordable_ticket([50, 75, 100, 150], 90)
assert res == 1