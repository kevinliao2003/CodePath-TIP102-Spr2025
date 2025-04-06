from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

# Advanced Problem Set Version 1 - Problem 2: Flower Finding
def find_flower(inventory, name):
    """
    U - Understand
    - plants are organized according to their names in a binary search tree
    - determine if name is in the flower inventory
    - inventory is always valid

    M - Match
    - dfs

    P - Plan
    define a helper function
        parameters:
            - curr (current node)
        
        base case:
            - if curr is the target, return true
            - if curr is not valid, return false
        
        if curr > target recurse left
        if curr < target recurse right

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) to visit all nodes in the tree (assuming the tree isn't balanced)
    - SC: O(n)
    """

    def dfs(curr):
        if curr:
            print(curr.val)
        if curr and curr.val == name:
            return True
        elif curr and curr.val > name:
            return dfs(curr.left)
        elif curr and curr.val < name:
            return dfs(curr.right)
        else:
            return False
        
    return dfs(inventory)

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)
res = find_flower(garden, "Lilac")
assert res == True
res = find_flower(garden, "Sunflower")
assert res == False

# Advanced Problem Set Version 2 - Problem 6: Minimum Ocean Depth
def find_min_depth(root):
    """
    U - Understand
    - return the minimum depth
    - root is always valid?

    M - Match
    - dfs

    P - Plan
    define a helper method
        parameters:
            - curr (current node)
        
        base case:
            if curr is not valid, return 0

        return min(1 + dfs(curr.left), 1 + dfs(curr.right))

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the number of ndoes in the tree (in the worst case scenario when the tree isn't balanced)
    - SC: O(n)
    """

    def dfs(curr):
        if not curr:
            return 0
        
        return min(1 + dfs(curr.left), 1 + dfs(curr.right))
    
    return dfs(root)

values = ["Shipwreck", "Shallows", "Reef", None, None, "Cave", "Trench"]
ocean = build_tree(values)
res = find_min_depth(ocean)
assert res == 2