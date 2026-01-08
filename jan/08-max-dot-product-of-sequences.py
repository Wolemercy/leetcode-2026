# https://leetcode.com/problems/max-dot-product-of-two-subsequences

# T = O(n*m) S = O(n*m)
# 2D Dynamic Programming Problem, which I struggled with.
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