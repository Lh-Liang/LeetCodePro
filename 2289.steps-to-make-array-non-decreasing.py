#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Stack stores tuples of (value, steps)
        # steps = number of steps it took to remove this value
        # If a value is never removed, steps is 0 (though we only care about max steps)
        stack = []
        ans = 0
        
        for num in nums:
            current_steps = 0
            # We need to remove all elements smaller than or equal to current num 
            # that are to the left, because they would have been removed by 
            # the 'killer' (an element larger than num) to the left of them 
            # before the killer reaches num (or num reaches the killer).
            while stack and stack[-1][0] <= num:
                current_steps = max(current_steps, stack.pop()[1])
            
            # If the stack is not empty, it means there is a number larger than 'num'
            # to its left. This larger number will eventually remove 'num'.
            # The time it takes is max(steps of elements between them) + 1.
            if stack:
                current_steps += 1
                stack.append((num, current_steps))
                ans = max(ans, current_steps)
            else:
                # If stack is empty, 'num' is the largest seen so far in the current
                # non-decreasing prefix logic, so it won't be removed.
                stack.append((num, 0))
                
        return ans

# @lc code=end