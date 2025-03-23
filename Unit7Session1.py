# Advanced Problem Set Version 1 - Problem 1: Counting the Layers of a Sandwich
def count_layers(sandwich):
    """
    U - Understand
    - return the sandwich layers
    - assume valid input?
    - each layer is represented by a nested list

    M - Match
    - recursion

    P - Plan
    - recursive approach
        base case: if index > len(list) or the type of the parameter is not a list
            return 0
        
        return 1 + helper(idx + 1)

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the number of nested lists
    - SC: O(n) for the recursive stack
    """

    def helper(sandwich):
        if len(sandwich) == 1:
            return 1
        
        if len(sandwich) > 1:
            return 1 + helper(sandwich[1])
    
    return helper(sandwich)

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
res = count_layers(sandwich1)
assert res == 4
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
res = count_layers(sandwich2)
assert res == 5

# Advanced Problem Set Version 2 - Problem 2: Finding the Longest Sequence of Trident Gems
def longest_trident_sequence(gems):
    """
    U - Understand
    - gens are arranged in a sequence of integers representing their value
    - return the length of the consecutive sequence of gens where each subsequent value increases by 1
    - valid input? can the array be empty?

    M - Match
    - a heap would work, but we want to use recursion for this problem

    P - Plan
    helper function (params: idx, curr_length, max_length)
        base case: if idx == len(nums) - 2 return max_length

        if gems[idx] + 1 == gems[idx + 1]
            return recursive call with params (idx + 1, curr_length + 1, max(max_length, curr_length + 1))
        else
            return recursive call with params (idx + 1, 1, max_length)

    call the helper function

    I - Implement
    - see code below.

    R - Review
    - see test cases below.

    E - Evaluate
    - TC: O(n) where n is the size of the list since we'll visit each element at most once
    - SC: O(n) where n is the max size of the recursive call stack
    """

    def helper(idx, curr_length, max_length):
        if idx == len(gems) - 1:
            return max_length
        
        if gems[idx] + 1 == gems[idx + 1]:
            return helper(idx + 1, curr_length + 1, max(max_length, curr_length + 1))
        else:
            return helper(idx + 1, 1, max_length)
        
    return helper(0, 1, 1)

res = longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6])
assert res == 5
res = longest_trident_sequence([5, 10, 7, 8, 1, 2])
assert res == 2