from collections import deque

# Advanced Problem Set Version 1 - Problem 1: Get Flight Cost
def calculate_cost(flights, start, dest):
    """
    U - Understand
    - flights is a list of tuples (destination, cost)
    - return the total cost of flying from start to dest
    - if not possible, return -1
    - if there are multiple paths, return any of the answers

    M - Match
    - bfs

    P - Plan
    variables:
    - q (queue)
        in the format of a tuple (location, cost)

    perform the standard bfs algorithm

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of the dictionary
    - SC: O(n)
    """

    q = deque([(start, 0)])
    visited = set()
    while q:
        for _ in range(len(q)):
            location, cost = q.popleft()
            if location == dest:
                return cost
            visited.add(location)
            
            for nei_location, nei_cost in flights[location]:
                if nei_location not in visited:
                    q.append((nei_location, cost + nei_cost))
                    visited.add(nei_location)

    return -1 # no such path exists

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

res = calculate_cost(flights, 'LAX', 'MIA')
assert res == 550

# Advanced Problem Set Version 1 - Problem 6: Find All Flight Routes
def find_all_flight_routes(flight_routes):
    """
    U - Understand
    - find all paths from airport 0 to airport n - 1
    - return the answer in any order
    - return all possible flight paths from airport 0 to airport (n - 1)

    M - Match
    - dfs, backtracking

    P - Plan
    variables:
        - res (all flight routes to return)
        - path (current flight path)
        - visited set

    define a helper function (route)
        if the route is (n - 1)
            add a copy of the path to res
            return

        add the route to the path
        add it to the visited set
        go through all the neighbors
            if the neighbor hasn't been visited
                call the helper function
        backtrack

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of flight_routes
    - SC: O(n)
    """

    n = len(flight_routes)
    res, path = [], []
    visited = set()

    def dfs(airport):
        nonlocal n

        path.append(airport)

        if airport == n - 1:
            res.append(path.copy())
        else:
            for nei in flight_routes[airport]:
                dfs(nei)

        path.pop()

    dfs(0)
    return res

flight_routes_1 = [[1, 2], [3], [3], []]
res = find_all_flight_routes(flight_routes_1)
assert res == [[0, 1, 3], [0, 2, 3]]