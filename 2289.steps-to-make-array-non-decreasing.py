#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # stack will store pairs of (value, steps_to_be_removed)
        # steps_to_be_removed represents the step count at which this element is deleted.
        # If an element is never deleted, its steps_to_be_removed will be 0.
        stack = []
        max_steps = 0
        
        for x in nums:
            current_element_steps = 0
            # When we encounter an element x, we check elements to its left that are smaller or equal.
            # These elements would have been 'covered' or deleted before x could be deleted 
            # by the same larger element further to the left.
            while stack and stack[-1][0] <= x:
                # The time x takes to be deleted must be strictly greater than the time 
                # taken by any element 'blocked' by x.
                current_element_steps = max(current_element_steps, stack.pop()[1])
            
            if not stack:
                # No element to the left is larger than x; x survives.
                current_element_steps = 0
            else:
                # The element at the top of the stack is > x. 
                # x will be deleted one step after the last element between the 'killer' and x is gone.
                current_element_steps += 1
            
            stack.append((x, current_element_steps))
            max_steps = max(max_steps, current_element_steps)
            
        return max_steps
# @lc code=end