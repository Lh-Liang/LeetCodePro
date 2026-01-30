#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # Each element: (value, steps to remove)
        res = 0
        for num in nums:
            steps = 0
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack[-1][1])
                stack.pop()
            if stack:
                steps += 1
            else:
                steps = 0
            res = max(res, steps)
            stack.append((num, steps))
        return res
# @lc code=end