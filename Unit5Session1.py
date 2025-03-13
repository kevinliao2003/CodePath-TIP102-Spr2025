# Advanced Problem Set Version 1 - Problem 7: Fishing Probability
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    """
    U - Understand
    - each node has a fish name
    - return the probability of the fish of type fish_name being catched
    - the function accepts the head of the linked list

    M - Match
    - linked list

    P - Plan
    variables:
    - freq (how many times fish_name appears)
    - count (number of nodes in the list)

    start from head and loop until the end
        if fish_name is found
            increment freq
        increment count

    return freq / count

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of the list
    - SC: O(1)
    """

    freq = count = 0
    curr = head
    while curr:
        if curr.fish_name == fish_name:
            freq += 1
    
        curr = curr.next
        count += 1

    return round(freq / count, 2) # 2 decimal places

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
res = fish_chances(fish_list, "Dace")
assert res == 0.33
res = fish_chances(fish_list, "Rainbow Trout")
assert res == 0.00

# Advanced Problem Set Version 2 - Problem 6: Count Racers
class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def count_racers(head):
    """
    U - Understand
    - linked list structure
    - function accepts the head of the linked list
    - return the number of players in the race/length of the linked list

    M - Match
    - linked list

    P - Plan
    variables:
    - count (length of list)

    while there are still nodes
        increment count
        move the current pointer to the right

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of the list
    - SC: O(1)
    """

    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    return count

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")
res = count_racers(racers1)
assert res == 4
res = count_racers(racers2)
assert res == 1
res = count_racers(None)
assert res == 0