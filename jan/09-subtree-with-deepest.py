# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Struggled, but I was almost there. I'd erroneously assumed that whatever would be returned from
# the recursive function should be what's passed back into it. This is wrong, of course. I'd therefore tried
# tracking the deepest subtree in a global tree, but I didn't need to do that.
# This solution relies on tracking the deepest node, by counting from the leaf of the tree. So that at any level,
# we'd have access to the deepest node in that subtree and the current depth of the node we're at.
# T(n) = O(N) S(n) = O(H)

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            if left_depth == right_depth:
                return (node, left_depth + 1)
            
            if (left_depth > right_depth):
                return (left_node, left_depth + 1)

            else:
                return (right_node, right_depth + 1)

        deepest_node, max_depth = dfs(root)

        return deepest_node
