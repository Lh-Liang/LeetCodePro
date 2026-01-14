#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            # When going right to left with even count, head moves forward
            if not left_to_right and remaining % 2 == 0:
                head += step
            
            step *= 2
            remaining = (remaining + 1) // 2
            left_to_right = not left_to_right
        
        return head
# @lc code=end