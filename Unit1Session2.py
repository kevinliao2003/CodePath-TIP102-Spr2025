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

# Advanced Problem Set Version 1 - Problem 2: Two-Pointer Reverse List

# Advanced Problem Set Version 1 - Problem 5: Container with Most Honey

# Advanced Problem Set Version 1 - Problem 6: Merge Intervals

# Advanced Problem Set Version 2 - Problem 1: Matrix Addition
"""
U - Understand
- are both matrices guaranteed to have the same dimensions?
- function should return an n * m matrix

P - Plan
variables:
- new_matrix (n * m)

loop through the rows and cols
    add the values in the 2 matrices and set that new value to the curr_pos in new_matrix
return new_matrix

I - Implement
- see code below
"""

def add_matrices(matrix1, matrix2):
    ROWS, COLS = len(matrix1), len(matrix1[0])
    new_matrix = [[0] * COLS for row in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):
            new_matrix[row][col] = matrix1[row][col] + matrix2[row][col]
    return new_matrix

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# res = add_matrices(matrix1, matrix2)
# print(res == [
#     [10, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10]
# ])

# Advanced Problem Set Version 2 - Problem 2: Two-Pointer Palindrome
"""
U - Understand
- string consists of only lowercase alphabetic characters
- can the string be empty?

P - Plan
variables:
- left pointer
- right pointer

while left <= right
    if the chars at two pos are NOT equal
        return false
    otherwise
        increment left
        increment right
return True

I - Implement
- see code below
"""

def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True

# s = "madam"
# res = is_palindrome(s)
# print(res == True)

# s = "madamweb"
# is_palindrome(s)
# res = is_palindrome(s)
# print(res == False)

# Advanced Problem Set Version 2 - Problem 3: Squash Spaces
"""
U - Understand
- can the string be empty?
- can the string only consist of lower and uppercase letters?

P - Plan
variables:
- curr_idx: int
- new_str: str
- leading_spaces: bool

increment curr_idx if there are leading spaces
while curr_idx is in bounds
    if the curr char is NOT a space
        if leading_spaces is true
            add a single space to new_str
            set leading_zeros to false
        add the curr char to new_str
    else if the curr char is a space
        set leading_zeros to true
    
    increment curr_idx

I - Implement
- see code below
"""

def squash_spaces(s):
    n = len(s)
    curr_idx = 0
    new_str = ""
    leading_spaces = False

    # trailing spaces
    while curr_idx < n:
        if s[curr_idx] == ' ':
            curr_idx += 1
        else:
            break

    while curr_idx < n:
        if s[curr_idx] != ' ':
            if leading_spaces:
                new_str += ' '
                leading_spaces = False
            new_str += s[curr_idx]
        else:
            leading_spaces = True
        
        curr_idx += 1
    
    return new_str

# s = "   Up,     up,   and  away! "
# res = squash_spaces(s)
# print(res == "Up, up, and away!")
# s = "With great power comes great responsibility."
# res = squash_spaces(s)
# print(res == "With great power comes great responsibility.")