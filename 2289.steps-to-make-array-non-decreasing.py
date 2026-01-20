#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

from typing import List

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(n):
            cur_steps = 0
            while stack and nums[stack[-1]] <= nums[i]:
                cur_steps = max(cur_steps, dp[stack.pop()])
            if stack:
                dp[i] = cur_steps + 1
            ans = max(ans, dp[i])
            stack.append(i)
        return ans
# @lc code=end