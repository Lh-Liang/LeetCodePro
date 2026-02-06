#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # will store pairs of (number, steps)
        max_steps = 0
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            current_steps = 0
            # Pop all elements from stack which are smaller than current element
            while stack and nums[i] > stack[-1][0]:
                current_steps = max(current_steps + 1, stack[-1][1])
                stack.pop()
            
            max_steps = max(max_steps, current_steps)
            # Append current number with its count of steps required to remove it completely (if ever needed)
            stack.append((nums[i], current_steps))
        return max_steps
# @lc code=end