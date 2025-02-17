# Advanced Problem Set Version 1 - Problem 3: T-I-Double Guh-Er II
"""
U - Understand
- lowercase v uppercase letters?
- can word be empty?
- will word only have lower and uppercase English letters?

P - Plan
variables
- idx (current index)
- new_str (new string to return)

while idx is in bounds
    if idx + 1 is in bounds and the substring at word[idx:idx+2] is 'gg' or 'er'
        increment idx by 2
    otherwise if curr char is t or i
        increment idx by 1
    else
        add curr char to new_str
return new_str

I - Implement
- see code below
"""

def tiggerfy(word):
    n = len(word)
    idx = 0 # current index
    new_str = "" # new string to return

    while idx < n:
        if idx + 1 < n:
            substr = word[idx:idx+2].lower()
            if substr == 'gg' or substr == 'er':
                idx += 2
                continue

        if word[idx] in 'tiTI':
            idx += 1
        else:
            new_str += word[idx]
            idx += 1
        # print(idx, new_str)
    return new_str

# word = "Trigger"
# res = tiggerfy(word)
# print(res)
# print(res == "r")
# word = "eggplant"
# res = tiggerfy(word)
# print(res)
# print(res == "eplan")
# word = "Choir"
# res = tiggerfy(word)
# print(res == "Chor")

# Advanced Problem Set Version 2 - Problem 7: Diagonal
"""
U - Understand
- with the matrix only consist of integers?
- all rows have the same number of cols?
- can the matrix be empty?
- the matrix is a square

P - Plan
grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]

primary diagonal pos: (0, 0), (1, 1), (2, 2), (3, 3)
secondary diagonal pos: (0, 3), (1, 2), (2, 1), (3, 0)

conditions
add the value to the total if the position:
- x and y coordinates are the same
- the sum of the x and y coordinates equal n

I - Implement
- see code below.
"""

def diagonal_sum(grid):
    n = len(grid)
    total = 0 # diagonal sum to return

    for row in range(n):
        for col in range(n):
            if row == col or row + col == n - 1:
                # print(row, col)
                total += grid[row][col]
    return total

# grid = [
# 	[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# res = diagonal_sum(grid)
# print(res)
# print(res == 25)
# grid = [
# 	[1, 1, 1, 1],
#     [1, 1, 1, 1],
# 	[1, 1, 1, 1],
#     [1, 1, 1, 1]
# ]
# res = diagonal_sum(grid)
# print(res == 8)
# grid = [
# 	[5]
# ]
# res = diagonal_sum(grid)
# print(res == 5)

# Advanced Problem Set Version 2 - Problem 8: Local Maximums
"""
U - Understand
- matrix is guaranteed to be a square
- elements are guaranteed to be ints

P - Plan
variables
- new matrix ((n - 2) * (n - 2))

loop through original matrix
    check the elements in the next 2 rows and cols
    update the val at current index in new matrix with the max value
return new matrix

I - Implement
- see code below
"""

def local_maximums(grid):
    ROWS, COLS = len(grid), len(grid[0])
    new_matrix = [[0] * (COLS - 2) for row in range(ROWS - 2)]

    for row in range(ROWS - 2):
        for col in range(COLS - 2):
            # print(row, col)
            # check 3 x 3 matrix
            curr_max = grid[row][col]
            for row2 in range(row, row + 3):
                for col2 in range(col, col + 3):
                    curr_max = max(curr_max, grid[row2][col2])
            
            new_matrix[row][col] = curr_max

    return new_matrix

# grid = [
# 	[9, 9, 8, 1],
# 	[5, 6, 2, 6],
# 	[8, 2, 6, 4],
# 	[6, 2, 2, 2]
# ]
# res = local_maximums(grid)
# print(res)
# print(res == [[9, 9], [8, 6]])
# grid = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 2, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1]
# ]
# res = local_maximums(grid)
# print(res == [[2, 2, 2], [2, 2, 2], [2, 2, 2]])