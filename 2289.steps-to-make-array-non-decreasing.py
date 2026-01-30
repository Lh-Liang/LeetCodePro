# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # To store (element, steps) pairs
        max_steps = 0  # To track maximum steps taken
        for num in nums:
            current_steps = 0
            # Remove all elements from stack which are less than or equal to current num
            while stack and stack[-1][0] <= num:
                current_steps = max(current_steps, stack.pop()[1])
            # If there are still elements in the stack after popping,
            # it means current num needs one more step compared to those popped because it causes a decrease
            if stack:
                current_steps += 1
            max_steps = max(max_steps, current_steps)
            # Push current num with its step count onto stack
            stack.append((num, current_steps))
        return max_steps
# @lc code=end