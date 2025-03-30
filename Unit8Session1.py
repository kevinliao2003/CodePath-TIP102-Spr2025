# Advanced Problem Set Version 1 - Problem 1: Ivy Cutting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    """
    U - Understand
    - return a list with the value of each node from the root node to the rightmost node
    - root node is valid
    - is the binary tree balanced?

    M - Match
    - dfs

    P - Plan
    variables:
        - res (list to return)

    define a recursive helper method
        parameters:
            - curr (current node)
        
        base case:
            if curr is invalid, return

        add the value to res
        recurse on the right subtree

    call the helper method
    return res

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the number of nodes in the tree
    - SC: O(n)
    """

    # res = [] # list to return
    # def dfs(curr):
    #     if not curr:
    #         return

    #     res.append(curr.val)
    #     dfs(curr.right)

    # dfs(root)
    # return res

    result = []
    current = root
    
    while current:
        result.append(current.val)
        if current.right:
            current = current.right
        else:
            break

    return result

ivy1 = TreeNode("Root", 
            TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2", TreeNode("Leaf3"))))
res = right_vine(ivy1)
# print(res)
assert res == ['Root', 'Node2', 'Leaf3']
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
res = right_vine(ivy2)
assert res == ['Root']