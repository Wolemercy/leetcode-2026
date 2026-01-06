# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Attempt 1
# Intuition: Perform a level order traversal of the tree while keeping track of the sum at each level.
# T = O(n) S = O(w) where w is the maximum width of the and n is the number of nodes in the tree
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        smallest_level = 1
        max_sum = root.val

        parent_nodes = [root]
        child_nodes = []

        curr_level = 1
        curr_sum = 0

        while len(parent_nodes):
            curr = parent_nodes.pop()
            curr_sum += curr.val

            if curr.left:
                child_nodes.append(curr.left)
            
            if curr.right:
                child_nodes.append(curr.right)

            if len(parent_nodes) == 0:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    smallest_level = curr_level
                
                parent_nodes = child_nodes
                child_nodes = []
                curr_level += 1
                curr_sum = 0
        
        return smallest_level

# Attempt 2
# Now using deque for efficient popping from the front of the queue
# T = O(n) S = O(w)
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        best_level = 0
        max_sum = float('-inf')

        queue = deque([root])

        curr_level = 0

        while len(queue):
            curr_level += 1
            curr_sum = 0
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                best_level = curr_level
            
        return best_level