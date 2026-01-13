#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # stack of (value, steps_to_remove)
        max_steps = 0
        
        for num in nums:
            steps = 0
            # Pop all elements that are <= current element
            while stack and stack[-1][0] <= num:
                steps = max(steps, stack[-1][1])
                stack.pop()
            
            # If stack is not empty, current element will be removed
            if stack:
                steps += 1
            
            stack.append((num, steps))
            max_steps = max(max_steps, steps)
        
        return max_steps
# @lc code=end