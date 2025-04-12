from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

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

# Advanced Problem Set Version 1 - Problem 2: Cookie Sum
def count_cookie_paths(root, target_sum):
    """
    U - Understand
    - return the number of unique paths from root to a leaf node where the number of cookies is target_sum
    - is the tree valid?

    M - Match
    - dfs

    P - Plan
    variables:
        - count (number of cookie paths to return)

    helper function (parameters: curr, sum)
        if curr is a leaf
            if sum is equal to target
                increment count
            return

        call on left subtree, adding curr.val to sum
        call on right subtree, adding curr.val to sum

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) since we're processing each node once
    - SC: O(n)
    """

    def dfs(curr, curr_sum):
        if not curr:
            return 0
        
        curr_sum += curr.val

        if not curr.left and not curr.right:
            return 1 if curr_sum == target_sum else 0
        
        return dfs(curr.left, curr_sum) + dfs(curr.right, curr_sum)
        
       
    return dfs(root, 0)

cookie_nums = [10, 5, 8, 3, 7, 12, 4]
cookies1 = build_tree(cookie_nums)
cookie_nums = [8, 4, 12, 2, 6, None, 10]
cookies2 = build_tree(cookie_nums)

res1 = count_cookie_paths(cookies1, 22)
assert res1 == 2
res2 = count_cookie_paths(cookies2, 14)
assert res2 == 1

# Advanced Problem Set Version 2 - Problem 1: Largest Pumpkin in Each Row
def largest_pumpkins(pumpkin_patch):
    """
    U - Understand
    - is the root always valid?
    - return an array of the largest pumpkin in each row
    - each level represents a row of pumpkins
    - tree isn't guaranteed to be balanced

    M - Match
    - bfs

    P - Plan
    bfs approach using a queue

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) since we iterate over each node once
    - SC: O(1), excluding the output array
    """

    q = deque([pumpkin_patch])
    res = [] # list to return
    while q:
        curr_max = float('-inf') # max value in each row
        for _ in range(len(q)):
            curr = q.popleft()
            curr_max = max(curr_max, curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        res.append(curr_max)

    return res

pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)
res = largest_pumpkins(pumpkin_patch)
assert res == [1, 3, 9]