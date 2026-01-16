# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field

# Definitely need to revisit this problem later
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        h_gaps = set()
        hFences.sort()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_gaps.add(hFences[j] - hFences[i])
        
        vFences.sort()
        max_side = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                gap = vFences[j] - vFences[i]
                if gap in h_gaps:
                    max_side = max(max_side, gap)
        
        if max_side == -1:
            return -1
            
        return (max_side * max_side) % MOD