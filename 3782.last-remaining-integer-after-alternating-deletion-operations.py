#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        s, d, m = 1, 1, n
        turn = 1  # 1: op1 (left), 0: op2 (right)
        while m > 1:
            if turn == 1:
                # op1: s unchanged
                d *= 2
                m = (m + 1) // 2
            else:
                # op2
                if m % 2 == 0:
                    s += d
                d *= 2
                m = (m + 1) // 2
            turn = 1 - turn
        return s
# @lc code=end