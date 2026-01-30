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
        left = True
        remaining = n
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left = not left
        return head
# @lc code=end