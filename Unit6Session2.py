import random

# Advanced Problem Set Version 1 - Problem 4: Shared Music Taste
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def playlist_overlap(playlist_a, playlist_b):
    """
    U - Understand
    - no cycle in the linked list
    - we're given 2 singly linked lists (the heads)
    - if no intersection, return None

    M - Match
    - linked list, 2 pointers

    P - Plan
    variables:
    - pointerA (pointer in playlist_a)
    - pointerB (pointer in playlist_b)

    while pointerA != pointerB
        if not pointerA
            set it to the head of playlist_B
        else
            shift pointerA to the right

        if not pointerB
            set it to the head of playlist_A
        else
            shift pointerB to the right

    return pointerA
    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of the list
    - SC: O(1)
    """

    pointerA, pointerB = playlist_a, playlist_b
    while pointerA != pointerB:
        if not pointerA:
            pointerA = playlist_b
        else:
             pointerA = pointerA.next

        if not pointerB:
             pointerB = playlist_a
        else:
             pointerB = pointerB.next

    return pointerA

playlist_a = Node('Song A', Node('Song B'))
playlist_b = Node('Song X', Node('Song Y', Node('Song Z')))
shared_segment = Node('Song M', Node('Song N', Node('Song O')))
playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment
res = (playlist_overlap(playlist_a, playlist_b)).value
assert res == 'Song M'

# Advanced Problem Set Version 2 - Problem 2: Surprise Me
def get_random(playlist):
    """
    U - Understand
    - return a random node
    - each node must have the same probability of being chosen
    - there is at least 1 node in the list

    M - Match
    - linked list

    P - Plan
    variables:
    - count (number of nodes in the list)
    - curr (current node)
    - res (result node to return)

    while curr
        get a random number from 0 to count
        if it's 0
            set the res to the current node
        move curr to the right
        increment count

    return res

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the number of nodes in the list
    - SC: O(1)
    """

    res, curr = None, playlist
    count = 0
    while curr:
        if random.randint(0, count) == 0:
            res = curr.value
        curr = curr.next
        count += 1
    
    return res

catalogue = Node(('Homegoing', 'Yaa Gyasi'), 
                Node(('Pachinko', 'Min Jin Lee'),
                         Node(('The Night Watchman', 'Louise Erdrich'))))

print(get_random(catalogue))