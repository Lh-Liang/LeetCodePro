#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        a = 1          # first element of current arithmetic progression
        step = 1       # difference between consecutive elements
        m = n          # how many elements remain
        left = True    # True => operation 1 (from left), False => operation 2 (from right)

        while m > 1:
            if left:
                # Operation 1: keep first, remove every 2nd from left
                m = (m + 1) // 2
                step *= 2
            else:
                # Operation 2: keep last, remove every 2nd from right
                if m % 2 == 0:
                    a += step
                m = (m + 1) // 2
                step *= 2
            left = not left

        return a
# @lc code=end
