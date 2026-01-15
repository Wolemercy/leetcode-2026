# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid

# The approach is to find the largest consecutive gaps in the horizontal and vertical bars.
# The maximum size of the square hole that can be formed is determined by the smaller of these two gaps.
# We need to sort the bar positions to achieve this.
# Key to remember that when a bar is removed, its "absence" is felt throughout the grid
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_gap(bars):
            bars.sort()
            max_consecutive_bars = 1

            consecutive_bars = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    consecutive_bars += 1
                else:
                    consecutive_bars = 1
                max_consecutive_bars = max(max_consecutive_bars, consecutive_bars)
                    
            return max_consecutive_bars + 1

        h_gap = get_gap(vBars)
        v_gap = get_gap(hBars)

        return min(h_gap, v_gap) ** 2
