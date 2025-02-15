# Standard Problem Set Version 1 - Problem 7: Good Things Come in Threes
"""
U - Understand
- can the array be empty? can the integers be + and -?
- is there a limit on the number of operations?
- all elements must be divisible by 3

P - Plan
variables
- total count

iterate though the array
    if curr num divisible by 3, do nothing
    otherwise
        find the nearest element divisible by 3 less than curr num
        find the nearest element divisible by 3 greater than curr num

        compare the absolute value and see which one needs fewer operations
        add to total count that absolute value
return total count

I - Implement
- see code below
"""

def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            left_num = num - 1
            while left_num % 3 != 0:
                left_num -= 1

            right_num = num + 1
            while right_num % 3 != 0:
                right_num += 1

            left_diff = abs(left_num - num)
            right_diff = abs(right_num - num)
            count += min(left_diff, right_diff)

    return count

# nums = [1, 2, 3, 4]
# res = make_divisible_by_3(nums)
# print(res == 3)

# nums = [3, 6, 9]
# res = make_divisible_by_3(nums)
# print(res == 0)

# Standard Problem Set Version 2 - Problem 3: Secret Identity
"""
U - Understand
- are all names in people strings?
- can any of the names by empty?
- will the names consist of spaces, and only lower and uppercase characters?
- is the secret_identity guaranteed to be in people?
- can the secret_identity by empty?
- must edit the array in place

P - Plan
variables
- curr_idx: current index

while curr_idx < len(people)
    if the current name is a match
        remove elem at curr_idx
    else
        increment curr_idx
return people

I - Implement
- see code below
"""

def remove_name(people, secret_identity):
    curr_idx = 0
    while curr_idx < len(people):
        if people[curr_idx] == secret_identity:
            del people[curr_idx]
        else:
            curr_idx += 1
    return people

# people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
# secret_identity = 'Bruce Wayne'
# res = remove_name(people, secret_identity)
# print(res == ['Batman', 'Superman', 'The Riddler'])

# Advanced Problem Set Version 1 - Problem 1: Transpose Matrix
"""
U - Understand
- Can the matrix be empty?
- Do all rows have the same number of cols?
- Are all the elems in the matrix ints?

P - Plan
figure out the dimensions of the new matrix
loop through the original matrix
    for each (row, col), set the value in (col, row) in the new matrix to the current value
return the new matrix

I - Implement
- see code below
"""

def transpose(matrix):
    new_matrix = [[0] * len(matrix) for col in range(len(matrix[0]))]
    ROWS, COLS = len(new_matrix), len(new_matrix[0])

    for row in range(ROWS):
        for col in range(COLS):
            new_matrix[row][col] = matrix[col][row]
    return new_matrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# res = transpose(matrix)
# # print(res)
# print(res == [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ])

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# res = transpose(matrix)
# print(res == [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ])

# TO DO

# Advanced Problem Set Version 1 - Problem 2: Two-Pointer Reverse List

# Advanced Problem Set Version 1 - Problem 5: Container with Most Honey

# Advanced Problem Set Version 1 - Problem 6: Merge Intervals