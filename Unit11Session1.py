from collections import deque, defaultdict

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
    - TC: O(m * n)
    - SC: O(m * n)
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

# Advanced Problem Set Version 2 - Problem 2: Walls and Gates
def walls_and_gates(castle):
    """
    U - Understand
    - 3 possible values (1, 0, float('inf'))
    - return the modified matrix where each empty room is its distance to its nearest gate

    M - Match
    - bfs

    P - Plan
    variables:
    - q (queue)
        tuple format: (row, col, distance)
    - dic (dictionary to map each empty room to distance to nearest gate)

    loop through the castle to add all empty rooms to the queue

    loop through q
        pop from the queue
        check all 4 directions
            if in bounds is empty
                update the nearest distance
                append to the queue

    loop through the dictionary and update the empty matrices
    return the modified castle

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(m * n) to loop over all positions in the castle
    - SC: O(m * n)
    """

    ROWS, COLS = len(castle), len(castle[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def in_bounds(row, col):
        return 0 <= row < ROWS and 0 <= col < COLS

    q = deque()
    for row in range(ROWS):
        for col in range(COLS):
            if castle[row][col] == 0:
                q.append((row, col, 0))

    visited = set() # avoid duplicates
    while q:
        for _ in range(len(q)):
            row, col, distance = q.popleft()
            if (row, col) in visited:
                continue

            visited.add((row, col))

            for x, y in directions:
                new_row, new_col = row + x, col + y
                if in_bounds(new_row, new_col) and castle[new_row][new_col] == float('inf'):
                    castle[new_row][new_col] = min(castle[new_row][new_col], distance + 1)
                    q.append((new_row, new_col, castle[new_row][new_col]))

    return castle

castle = [
    [float('inf'), -1, 0, float('inf')],            # Row 0
    [float('inf'), float('inf'), float('inf'), -1], # Row 1
    [float('inf'), -1, float('inf'), -1],           # Row 2
    [0, -1, float('inf'), float('inf')]             # Row 3
    ]

res = walls_and_gates(castle)
print(res)