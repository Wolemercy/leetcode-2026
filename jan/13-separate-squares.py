# https://leetcode.com/problems/separate-squares-i

# T = O(N * K) where N is the number of squares and K is the number of iterations for binary search; S = O(1)
# Binary search problem to find the horizontal line that separates the squares into two equal areas
# It helps to know that adjusting the horizontal line upwards increases the area below it, and it is therefore, monotonic
# Binary search is then used to find the line that gives half the total area. We iterate a fixed number of times to ensure precision.
from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(square[2] ** 2 for square in squares)
        
        low = min(square[1] for square in squares)
        high = max(square[1] + square[2] for square in squares)

        for i in range(100):
            mid = 0.5*(low + high)
            area = 0

            for square in squares:
                x, y, l = square
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area += l ** 2
                else:
                    area += (mid - y) * l
            if (area < total_area / 2):
                low = mid
            else:
                high = mid
        
        return low

