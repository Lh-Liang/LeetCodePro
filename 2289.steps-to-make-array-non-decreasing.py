#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Stack stores tuples of (value, steps)
        stack = []
        max_steps = 0
        # Iterate from right to left through nums
        for num in reversed(nums):
            current_steps = 0
            # Resolve current element with stack top until it becomes valid
            while stack and num > stack[-1][0]:
                current_steps = max(current_steps + 1, stack.pop()[1])
            max_steps = max(max_steps, current_steps)
            stack.append((num, current_steps))
        return max_steps
# @lc code=end