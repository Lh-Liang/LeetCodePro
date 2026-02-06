#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        step = 1
        start = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                start += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
        
        return start
# @lc code=end