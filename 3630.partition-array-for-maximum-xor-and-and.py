#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
from typing import List

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        def backtrack(index, xor_a, and_b, xor_c):
            # Base case: if we've considered all numbers
            if index == len(nums):
                return xor_a + and_b + xor_c
            
            # Recursive case: choose current number for either A, B or C
            num = nums[index]
            
            # Case 1: Add num to A (XOR operation)
            max_value = backtrack(index+1, xor_a ^ num, and_b, xor_c)
            
            # Case 2: Add num to B (AND operation)
            new_and_b = (and_b & num) if and_b != -1 else num # -1 signifies empty B initially
            max_value = max(max_value, backtrack(index+1, xor_a, new_and_b, xor_c))
            
            # Case 3: Add num to C (XOR operation)
            max_value = max(max_value, backtrack(index+1, xor_a, and_b, xor_c ^ num))
            
            return max_value
        
        return backtrack(0, 0, -1, 0)
# @lc code=end