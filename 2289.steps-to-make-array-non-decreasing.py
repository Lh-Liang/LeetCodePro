#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # This will store pairs of (value, steps needed)
        max_steps = 0
        
        # Process each number in nums
        for num in nums:
            steps = 0  # Steps required to remove current number if needed
            # Remove all elements from stack that are greater than current num
            while stack and stack[-1][0] <= num:
                steps = max(steps, stack.pop()[1])  # Capture max steps needed from popped element
            
            # If stack is empty, no need of further steps as no prior greater element exists now
            if not stack:
                steps = 0
            else:
                steps += 1  # One additional step needed to remove this as previous element is greater
            
            max_steps = max(max_steps, steps)  # Update global max steps count as required for result
            
            # Push current element into the stack with its calculated step count requirement
            stack.append((num, steps))
        
        return max_steps
# @lc code=end