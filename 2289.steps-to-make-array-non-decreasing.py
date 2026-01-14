#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # (value, step)
        result = 0
        
        for num in nums:
            max_step = 0
            while stack and stack[-1][0] <= num:
                _, step = stack.pop()
                max_step = max(max_step, step)
            
            if stack:  # there's a larger element to the left that will eat this one
                step = max_step + 1
            else:
                step = 0  # no larger element to the left, this element survives
            
            result = max(result, step)
            stack.append((num, step))
        
        return result
# @lc code=end