#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        steps = [0] * n  # To store steps needed at each index.
        max_steps = 0
        
        for i in range(n):
            # While current element is greater than element at stack top,
            # pop from stack and calculate steps needed.
            while stack and nums[stack[-1]] > nums[i]:
                last_index = stack.pop()
                steps[i] = max(steps[i], steps[last_index] + 1)
            max_steps = max(max_steps, steps[i])
            stack.append(i)
        
        return max_steps
# @lc code=end