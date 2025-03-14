# Advanced Problem Set Version 1 - Problem 1: Greatest Node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    """
    U - Understand
    - find the maximum value in the linked list
    - we're given the head
    - linked list only has numeric values

    M - Match
    - linked list

    P - Plan
    variables:
    - curr_max (current maximum value in the list)
    - curr (current node, initialize with head)

    while curr is valid
        update curr_max
        move curr to right

    return curr_max

    I - Implement
    - see code below.

    R - Review
    - see test cases below.

    E - Evaluate
    - TC: O(n) where n is the size of the linked list
    - SC: O(1)
    """

    curr_max = 0
    curr = head
    while curr:
        curr_max = max(curr_max, curr.value)
        curr = curr.next

    return curr_max

head1 = Node(5, Node(6, Node(7, Node(8))))
assert find_max(head1) == 8
head2 = Node(5, Node(8, Node(6, Node(7))))
assert find_max(head2) == 8

# Advanced Problem Set Version 1 - Problem 3: Delete Duplicates in a Linked List
def delete_dupes(head):
    """
    U - Understand
    - linked list is sorted
    - delete all elements that occur more than once
    - all values are numeric
    - is the list guaranteed to have at least 1 element?

    M - Match
    - linked list, 2 pointers

    P - Plan
    - delete elements in place

    variables:
    - prev (head)
    - curr (head.next)

    append a temp head to the list
    while prev and curr
        while curr.next and curr.next.val == curr.val
            move curr to the right

        prev = curr
        curr = curr.next

    return the head

    I - Implement
    - see code below

    R - Review
    - review test cases below

    E - Evaluate
    - TC: O(n) where n is the number of nodes
    - SC: O(1)
    """

    tmp_head = Node(0, head)

    curr = tmp_head
    while curr:
        nxt = curr.next
        while nxt and nxt.next and nxt.next.value == nxt.value:
            nxt = nxt.next

        if curr.next != nxt: # duplicates found
            curr.next = nxt.next
            curr = curr.next
        else: # no duplicates
           curr = curr.next

    return tmp_head.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
print_linked_list(delete_dupes(head))
head = Node(1, Node(1, Node(1, Node(1, Node(1, Node(1))))))
print_linked_list(delete_dupes(head))