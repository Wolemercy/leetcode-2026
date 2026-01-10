# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings


# Attempt 1
# Needed to use memoization to optimize the recursive solution.
# The idea is to use a recursive function that compares characters from both strings.
# If the characters match, we move to the next characters in both strings.
# If they don't match, we have two options: delete the character from s1 or s2,
# and we take the minimum ASCII sum of these two options.
from functools import lru_cache
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def get_sum(i, j):
            if i == len(s1):
                return sum([ord(char) for char in s2[j:]])
            
            if j == len(s2):
                return sum([ord(char) for char in s1[i:]])
            
            if s1[i] == s2[j]:
                return get_sum(i+1, j+1)
            
            return min(ord(s1[i]) + get_sum(i+1, j), ord(s2[j]) + get_sum(i, j+1))
        
        return get_sum(0,0)
    
# Alternate DP Solution
# T = O(n1*n2) S = O(n1*n2)
# The idea is to use a 2D DP table where dp[i][j] represents the minimum ASCII delete sum
# to make the substrings s1[i:] and s2[j:] equal.
# We fill the table in a bottom-up manner, starting from the end of both strings.
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for j in range(n2-1, -1, -1):
            dp[n1][j] = dp[n1][j+1] + ord(s2[j])
            
        for i in range(n1-1, -1, -1):
            dp[i][n2] = dp[i+1][n2] + ord(s1[i])

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])
        
        return dp[0][0]

