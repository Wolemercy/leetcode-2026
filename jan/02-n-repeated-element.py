# https://leetcode.com/problems/n-repeated-element-in-size-2n-array

# Attempt 1
# T = O(n) S = O(n)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        
        nums_frequency = {}

        for num in nums:
            if num in nums_frequency:
                nums_frequency[num] += 1
                continue
            nums_frequency[num] = 1
            
        for k,v in nums_frequency.items():
            if v == n:
                return k
            
# Optimized Solution
# T = O(n) S = O(1)
# Relies on the fact that in an array of size 2n with n+1 unique elements,
# then the "majority" element is the only one that appears more than once. It also
# takes advantage of the fact that in any 4-length window, the repeated element must appear at least twice.
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            if (nums[i] == nums[i+1] or nums[i] == nums[i+2]):
                return nums[i]
        return nums[-1]