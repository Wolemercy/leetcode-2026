# https://leetcode.com/problems/four-divisors

# Attempt 1
# T = O(n * m) S = O(1)
# where n is the length of nums and m is the maximum number in nums
# Time Limit Exceeded because for each number we may have to check up to half of its value to find divisors
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # For each number, find and store the number of divisors it has and stop if it exceeds 4.
        def get_divisors(num: int):
            divisors = set()
            divisor = 1
            while divisor < num // 2 and len(divisors) <= 4:
                divisor_pair, remainder = num // divisor, num % divisor
                if remainder == 0:
                    divisors.add(divisor)
                    divisors.add(divisor_pair)
                divisor += 1
            
            return sum(divisors), len(divisors)

        sum_of_divisors = 0

        for num in nums:
            divisors_sum, divisors_count = get_divisors(num)
            if divisors_count == 4:
                sum_of_divisors += divisors_sum
        
        return sum_of_divisors
    
# Approach 2
# T = O(n * sqrt(m)) S = O(1)
# where n is the length of nums and m is the maximum number in nums
# For each number, we only check for divisors up to its square root.
# Why? Because a number has 4 divisors only if it is of the form
# - p^3 (where p is prime)  -> divisors: 1, p, p^2, p^3
# - p*q (where p and q are distinct primes) -> divisors: 1, p, q, p*q
# In both cases, the divisors can be found by checking up to the square root of the number.
# Because in a division pair (d, n/d), at least one of the pair must be less than or equal to sqrt(n).
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(num: int):
            divisors = set()
            divisor = 1
            while divisor * divisor <= num and len(divisors) <= 4:
                if num % divisor == 0:
                    divisors.add(divisor)
                    divisors.add(num // divisor)
                divisor += 1
            
            return sum(divisors), len(divisors)

        sum_of_divisors = 0

        for num in nums:
            divisors_sum, divisors_count = get_divisors(num)
            if divisors_count == 4:
                sum_of_divisors += divisors_sum
        
        return sum_of_divisors
    
# Simplified Approach 2.1
# T = O(n * sqrt(m)) S = O(1)
# where n is the length of nums and m is the maximum number in nums
# Similar to Approach 2 but simplifies the divisor counting logic.
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors_sum = 0

        for num in nums:
            divisors = set([1, num])
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    divisors.add(divisor)
                    divisors.add(num // divisor)
                    if len(divisors) > 4:
                        break
            
            if len(divisors) == 4:
                divisors_sum += sum(divisors)
            
        return divisors_sum