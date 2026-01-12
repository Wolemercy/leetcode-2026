# https://leetcode.com/problems/minimum-time-visiting-all-points

# Attempt 1 - Recursive Solution
# TLE on large inputs
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def visit(point1, point2):
            print(point1, point2)
            p1x, p1y = point1
            p2x, p2y = point2
            if p1x == p2x:
                return abs(p1y - p2y)
            
            if p1y == p2y:
                return abs(p1x - p2x)

            px, py = p1x, p1y
            
            px = p1x + 1 if p2x > p1x else p1x - 1
            py = p1y + 1 if p2y > p1y else p1y - 1

            return 1 + visit([px, py], [p2x, p2y])

        total_distance = 0
        for i in range(len(points) - 1):
            total_distance += visit(points[i], points[i+1])
        
        return total_distance

# Attempt 2
# T = O(n) S = O(1)
# The idea is to calculate the time taken to move from one point to the next
# by taking the maximum of the absolute differences in x and y coordinates if a diagonal
# move is possible. This is because a diagonal move covers both x and y distance in one
# time unit. If a diagonal move is not possible, we simply add the remaining distance
# in either x or y direction.
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def visit(point1, point2):
            p1x, p1y = point1
            p2x, p2y = point2

            total_time = 0

            while p1x != p2x or p1y != p2y:
                if p1x == p2x:
                    total_time += abs(p1y - p2y)
                    break
                
                if p1y == p2y:
                    total_time += abs(p1x - p2x)
                    break

                minDistance = min(abs(p2x - p1x), abs(p2y - p1y))
                
                p1x = p1x + minDistance if p2x > p1x else p1x - minDistance
                p1y = p1y + minDistance if p2y > p1y else p1y - minDistance
                total_time += minDistance
            return total_time

        total_distance = 0
        for i in range(len(points) - 1):
            total_distance += visit(points[i], points[i+1])
        
        return total_distance

# Optimal Solution
# T = O(n) S = O(1)
# The idea is to calculate the time taken to move from one point to the next
# by taking the maximum of the absolute differences in x and y coordinates
# This works because even when you move diagonally, you are effectively reducing both
# the x and y distances by 1 unit each time. Therefore, the total time taken to move from one point to another
# is determined by the larger of the two distances (x or y).
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            p1x, p1y = points[i]
            p2x, p2y = points[i+1]
            
            dx = abs(p1x - p2x)
            dy = abs(p1y - p2y)

            total_time += max(dx, dy)
        
        return total_time