#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Stack stores (value, steps_to_remove)
        stack = []
        max_steps = 0
        
        for x in nums:
            current_steps = 0
            # While current element is >= top of stack, it takes at least as many
            # steps as the elements it 'covers' to be removed by a larger element further left.
            while stack and stack[-1][0] <= x:
                prev_val, prev_steps = stack.pop()
                current_steps = max(current_steps, prev_steps)
            
            # If stack is not empty, the current top is strictly greater than x
            # and will eventually remove x.
            if stack:
                current_steps += 1
            else:
                # No element to the left is greater than x, so x is never removed.
                current_steps = 0
            
            stack.append((x, current_steps))
            max_steps = max(max_steps, current_steps)
            
        return max_steps
# @lc code=end