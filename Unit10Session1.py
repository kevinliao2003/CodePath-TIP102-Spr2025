from collections import deque

# Advanced Problem Set Version 1 - Problem 3: Finding All Reachable Destinations
def get_all_destinations(flights, city):
    """
    U - Understand
    - get all possible destinations from a starting point
    - direct or connecting flights
    - list should be in ascending order by number of layovers required
    - what about if the number of layovers is the same for 2 cities?

    M - Match
    - bfs

    P - Plan
    perform a bfs on the graph
    variables:
    - q (initialzie with city)
    - res (list to return with the cities)

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    """

    q = deque([city])
    visited = set() # avoid duplicates
    res = []

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in visited:
                continue

            visited.add(curr)
            res.append(curr)

            if curr in flights:
                for nei in flights[curr]:
                    q.append(nei)

    return res

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}
res = get_all_destinations(flights, "Beijing")
assert res == ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
res = get_all_destinations(flights, "Helsinki")
assert res == ['Helsinki', 'Cairo', 'New York', 'Reykjavik']

# Advanced Problem Set Version 1 - Problem 8: Number of Airline Regions
def num_airline_regions(is_connected):
    """
    U - Understand
    - we want to find the number of regions
    - return the total number of airline regions

    M - Match
    - dfs

    P - Plan
    variables:
    - visited (to keep track of the visited airports)
    - res (number of regions)

    create a dfs function
        parameters:
            - airport

        add it to the visited set
        if there is an airport connected and has not been visited
            add it to the visited set

    go through all airports
        if this is a new region and hasn't been visited
            call the helper function
            increment res

    return res

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    """

    n = len(is_connected)
    visited = set()
    res = 0

    def dfs(airport):
        visited.add(airport)
        for airport2 in range(n):
            if is_connected[airport][airport2] == 1 and airport2 not in visited:
                dfs(airport2)

    for airport in range(n):
        if airport not in visited:
            dfs(airport)
            res += 1
    
    return res

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

res = num_airline_regions(is_connected1)
assert res == 2
res = num_airline_regions(is_connected2)
assert res == 2