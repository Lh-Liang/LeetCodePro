#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # stack will store pairs of (value, steps_to_be_removed)
        stack = []
        max_steps = 0
        
        for x in nums:
            current_steps = 0
            # While the current element x is greater than or equal to the stack top,
            # x cannot be removed by the stack top. It must wait for the elements
            # that were being removed by the stack top's 'remover'.
            while stack and stack[-1][0] <= x:
                current_steps = max(current_steps, stack[-1][1])
                stack.pop()
            
            # If stack is empty, x is the largest element seen so far (or equal to it).
            # It will never be removed.
            if not stack:
                current_steps = 0
            else:
                # If stack is not empty, the current stack top is strictly greater than x.
                # x will be removed 1 step after all elements between the stack top and x are gone.
                current_steps += 1
            
            max_steps = max(max_steps, current_steps)
            stack.append((x, current_steps))
            
        return max_steps
# @lc code=end