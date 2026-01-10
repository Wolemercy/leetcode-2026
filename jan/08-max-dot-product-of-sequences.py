# https://leetcode.com/problems/max-dot-product-of-two-subsequences

# T = O(n*m) S = O(n*m)
# 2D Dynamic Programming Problem, which I struggled with.
# The idea is to use a 2D DP table where dp[i][j] represents the maximum dot product
# that can be obtained in the subarrays nums1[0..i-1] and nums2[0..j-1].
# This is a comparison of including or excluding the current elements from either array,
# and considering the product of the current elements.
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                current_product = nums1[i-1] * nums2[j-1]

                dp[i][j] = max(
                    current_product,
                    current_product + dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )
        
        return dp[n][m]