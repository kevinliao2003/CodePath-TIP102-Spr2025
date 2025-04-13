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

# Advanced Problem Set Version 1 - Problem 7: Number of Flights