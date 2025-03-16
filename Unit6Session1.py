# Advanced Problem Set Version 1 - Problem 2: Protein Folding Loop Detection
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    """
    U - Understand
    - return the nodes involved in the cycle
    - the head is guaranteed to be valid
    - if no cycle, return []

    M - Match
    - 2 pointers (turtoise and hair algo)

    P - Plan
    variables:
    - slow (head) - slow pointer
    - fast (head) - fast pointer
    - res (nodes to return)

    use turtoise and hair algo to find if a cycle exists
    - if a cycle exists, set the start of the cycle

    start from the node from where cycle starts
    while True
        add node to res
        increment the current node
        if the node is the start node
            break
            
    return res

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of the linked list
    - SC: O(1), excluding the output array
    """

    if not protein:
        return []
    
    slow, fast = protein, protein

    # find the cycle
    cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle = True
            break

    if not cycle: # no cycle detected
        return []
    
    # find the start node of the cycle
    slow = protein
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # build the res list to return
    res = []
    start = slow
    while True:
        res.append(slow.value)
        slow = slow.next
        if start == slow:
            break

    return res

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 
print(cycle_length(protein_head))

# Advanced Problem Set Version 2 - Problem 2: Cycle Start
def cycle_start(path_start):
    """
    U - Understand
    - given the head of a linked list
    - return the value of the node at the start of the loop
    - if no path exists, return None

    M - Match
    - 2 pointers (turtoise and hare algo)

    P - Plan
    variables:
    - slow (slow pointer)
    - fast (fast pointer)

    determine if there's a cycle in the linked list

    if there is, look for the start of the cycle

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: 
    - SC: 
    """
    
    if not path_start:
        return []

    # checks if there is a cycle
    slow, fast = path_start, path_start
    cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle = True
            break

    if not cycle: # no cycle detected
        return None
    
    slow = path_start
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.value

path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
res = cycle_start(path_start)
assert res == 'Point 1'