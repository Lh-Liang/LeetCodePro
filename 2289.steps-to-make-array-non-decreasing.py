#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Initialize variables
        max_steps = 0
        # Stack to hold pairs of (value, steps)
        stack = []
        # Iterating through each number in nums
        for num in nums:
            current_steps = 0
            # While stack is not empty and top of stack is greater than num
            while stack and stack[-1][0] <= num:
                current_steps = max(current_steps, stack.pop()[1])
            # If stack is not empty, increment steps for current number
            if stack:
                current_steps += 1
            else:
                current_steps = 0
            # Push current number with its steps onto the stack
            max_steps = max(max_steps, current_steps)
            stack.append((num, current_steps))
        return max_steps
# @lc code=end