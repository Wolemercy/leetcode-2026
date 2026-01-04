# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/

# Couldn't initially figure out the pattern, so I researched and found this approach
# T = O(n) S = O(1)
# The idea is to categorize the colorings into two types:
# 1. "ABA" type: where the first and third columns have the same color
# 2. "ABC" type: where all three columns have different colors
# For each subsequent row added to the grid:
# - An "ABA" type row can be followed by 3 "ABA" type rows (by changing the middle color)
#   or 2 "ABC" type rows (by changing all three colors).
# - An "ABC" type row can be followed by 2 "ABA" type rows (by changing the first or last color)
#   or 2 "ABC" type rows (by changing all three colors).
# We initialize the counts for a single row (n=1) as 6 for both "ABA" and "ABC" types.
# We then iteratively compute the counts for each additional row up to n,
# applying the transition rules and taking modulo 10^9 + 7 to prevent overflow.
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7

        aba = 6
        abc = 6

        for i in range(1, n):
            repeat_aba = (3 * aba) + (2 * abc)
            repeat_abc = (2 * aba) + (2 * abc)

            aba, abc = repeat_aba % mod, repeat_abc % mod
        
        return (aba + abc) % mod