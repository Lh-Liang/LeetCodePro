#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        def contains_no_zero(x):
            return '0' not in str(x)
        count = 0
        for a in range(1, (n // 2) + 1):
            b = n - a
            if contains_no_zero(a) and contains_no_zero(b):
                count += 1
        return count
# @lc code=end