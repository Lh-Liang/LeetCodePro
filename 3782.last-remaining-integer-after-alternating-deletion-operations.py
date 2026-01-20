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
        is_left = True
        
        while remaining > 1:
            if is_left:
                # Starting from left, we always keep the first element (head)
                # deleting every second number means we keep indices 0, 2, 4...
                # So head remains unchanged.
                pass
            else:
                # Starting from right
                # If remaining count is odd, the first element survives
                # (e.g., [1, 2, 3] -> keep 3, del 2, keep 1)
                # If remaining count is even, the first element is deleted
                # (e.g., [1, 2, 3, 4] -> keep 4, del 3, keep 2, del 1)
                if remaining % 2 == 0:
                    head += step
            
            step *= 2
            remaining = (remaining + 1) // 2
            is_left = not is_left
            
        return head
# @lc code=end