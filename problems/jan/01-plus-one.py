# https://leetcode.com/problems/plus-one

# Attempt 1
# T = O(n) S = O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        resulting_array = []
        
        carried_digit = 1
        for number in reversed(digits):
            new_item =  number + carried_digit
            number_to_add = new_item % 10
            if number_to_add == 0 and new_item >= 10:
                resulting_array.append(0)
                carried_digit = 1
            else:
                resulting_array.append(number_to_add)
                carried_digit = 0
        
        if carried_digit:
            resulting_array.append(carried_digit)
        result = resulting_array[::-1]
        return result
    
# Optimized Solution
# T = O(n) S = O(1)
# Relies on modifying the input array instead of creating a new one
# Simplifies the logic for carrying over digits because the resultant value is always the modulus
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carried_digit = 1

        for i in range(len(digits) - 1, -1, -1):
            plussed_value = digits[i] + carried_digit
            
            digits[i] = plussed_value % 10
            carried_digit = plussed_value // 10
        
        if carried_digit:
            digits = [1] + digits

        return digits