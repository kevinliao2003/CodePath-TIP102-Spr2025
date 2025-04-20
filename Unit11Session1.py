from collections import deque

# Advanced Problem Set Version 1 - Problem 1: Escape to the Safe Haven
def can_move_safely(position, grid):
    """
    U - Understand
    - we start at the position, specified in the parameter
    - 1s represent safe zones and 0s infected
    - return true if we can reach the safe heaven (the bottom most cell) and false otherwise
    - only 1s and 0s in the graph
    - 4 directions: left, right, up, down

    M - Match
    - bfs

    P - Plan
    variables:
    - q (queue)

    bfs algorithm
    - append position to the queue
    - for each position
        check all 4 directions
        check if they're in bounds and if it is safe
            add it to the queue

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: 
    - SC: 
    """

    ROWS, COLS = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def safe_and_valid(row, col):
        return 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1

    q = deque([position])
    visited = set() # avoid duplicates
    while q:
        for _ in range(len(q)):
            row, col = q.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return True
            
            if (row, col) not in visited:
                visited.add((row, col))
            else:
                continue

            for x, y in directions:
                new_row, new_col = row + x, col + y
                if safe_and_valid(new_row, new_col):
                    q.append((new_row, new_col))

    return False

grid = [
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)
res = can_move_safely(position_1, grid)
assert res == True
res = can_move_safely(position_2, grid)
assert res == True
res = can_move_safely(position_3, grid)
assert res == False