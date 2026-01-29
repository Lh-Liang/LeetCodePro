#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # stack stores pairs of (value, steps_to_remove)
        stack = []
        ans = 0
        
        for num in nums:
            max_steps_for_inner = 0
            # Pop elements that are smaller or equal to current num.
            # These are elements that were removed 'under' the same peak
            # or will be blocked by the current num.
            while stack and stack[-1][0] <= num:
                max_steps_for_inner = max(max_steps_for_inner, stack.pop()[1])
            
            if not stack:
                # This element is a new peak (nothing to its left is greater)
                stack.append((num, 0))
            else:
                # This element will be removed by the element currently at the top
                # It takes 1 step more than the maximum steps needed for any
                # element trapped between the 'remover' and this current element.
                steps_to_remove_num = max_steps_for_inner + 1
                ans = max(ans, steps_to_remove_num)
                stack.append((num, steps_to_remove_num))
                
        return ans
# @lc code=end