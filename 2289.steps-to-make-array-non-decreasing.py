#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # The stack will store tuples of (value, time_removed)
        # time_removed = 0 means the element is never removed.
        stack = []
        ans = 0
        
        for x in nums:
            t = 0
            # Pop elements that x is greater than or equal to.
            # We track the maximum time it took for those elements to be removed.
            while stack and stack[-1][0] <= x:
                t = max(t, stack.pop()[1])
            
            if not stack:
                # No element to the left is larger; x survives indefinitely.
                time_to_remove_x = 0
            else:
                # x will be removed by the current stack top element.
                # It takes 't' steps to clear previous elements, then 1 more for x.
                time_to_remove_x = t + 1
            
            stack.append((x, time_to_remove_x))
            ans = max(ans, time_to_remove_x)
            
        return ans
# @lc code=end