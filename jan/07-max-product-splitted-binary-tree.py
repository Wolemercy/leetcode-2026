# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Needed help here, as I somehow misunderstood the problem initially
# T(n) = O(n) S = O(n)
# The solution relies on calculating the sum of all subtrees first, then we iterate
# through the sums to calculate the maximum product of splitting at each subtree
# Really nifty solution
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtrees = []
        max_product = 0

        def get_sum(node):
            if not node:
                return 0
            
            subtree_sum = node.val + get_sum(node.left) + get_sum(node.right)
            subtrees.append(subtree_sum)
            return subtree_sum
        
        total_sum = get_sum(root)

        for s in subtrees:
            subtree_product = s * (total_sum - s)
            max_product = max(max_product, subtree_product)
        
        return max_product % (10**9 + 7)