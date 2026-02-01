#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # stack will store (value, steps_to_be_removed)
        stack = []
        ans = 0
        for x in nums:
            t = 0
            while stack and stack[-1][0] <= x:
                t = max(t, stack.pop()[1])
            
            if not stack:
                # x is the largest so far, won't be removed
                t = 0
            else:
                # x will be removed by stack[-1][0] at time t + 1
                t = t + 1
            
            ans = max(ans, t)
            stack.append((x, t))
        return ans
# @lc code=end