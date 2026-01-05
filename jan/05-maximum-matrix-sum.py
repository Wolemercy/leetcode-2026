# https://leetcode.com/problems/maximum-matrix-sum

# Could not initially solve this problem, so I researched and found this approach
# T = O(n^2) S = O(1)
# Given the ability to flip the sign of any two elements any number of times,
# the key thing to remember is that if you have an odd number of negative elements,
# you will be forced to have at least one negative element in the final sum. However,
# if you have an even number of negative elements, you can flip them all to positive.
# Therefore the max sum if the negative count is even is simply the sum of the absolute values
# of all elements. If the negative count is odd, then it means one negative element will remain.
# To minimize the impact of this negative element, we should choose the element with the smallest
# absolute value to be negative.
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_sum = 0
        negative_count = 0
        smallest_element = abs(matrix[0][0])

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                element = matrix[i][j]
                absolute_value = abs(element)
                matrix_sum += absolute_value

                smallest_element = min(smallest_element, absolute_value)

                if (element < 0):
                    negative_count += 1
        
        if negative_count % 2 == 1:
            matrix_sum += -2*smallest_element
        
        return matrix_sum