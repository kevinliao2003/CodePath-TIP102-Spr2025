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