from collections import deque

# Advanced Problem Set Version 1 - Problem 4: Find Next Order to Fulfill Today
class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def larger_order_tree(order_tree, order):
    """
    U - Understand
    - return the nearest node on the same level as order (next order to fulfill that day)
    - return none if order is the last order of the day (rightmost node of the level)
    
    M - Match
    - bfs

    P - Plan
    variables:
        - prev (the previous node)
            initialize to order
        - q (queue)
            initialize with order_tree

    bfs algorithm:
        while q
            for each element in q
                pop the leftmost element
                if the node is the order
                    if it's the last node on the level
                        return None
                    else
                        return the next node in the queu
                if the left child exists
                    add it to q
                    set prev to the popped element
                if the right child exists
                    add it to q
                    set prev to the left child element

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC:  O(n) since each element in the tree will be processed one
    - SC: O(n) since the q will have at most n elements
    """

    q = deque([order_tree])
    while q:
        n = len(q)
        for i in range(n):
            curr = q.popleft()
            if curr == order:
                if i == n - 1:
                    return None
                else:
                    return q.popleft()
                
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    return None

cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
assert next_order1.val == "Eclair"
assert next_order2 == None

# Advanced Problem Set Version 2 - Problem 2: Reverse Odd Levels of the Hotel