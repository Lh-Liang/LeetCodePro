#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for num in nums:
            steps = 0
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack[-1][1])
                stack.pop()
            if not stack:
                steps = 0
            else:
                steps += 1
            stack.append((num, steps))
            res = max(res, steps)
        return res
# @lc code=end