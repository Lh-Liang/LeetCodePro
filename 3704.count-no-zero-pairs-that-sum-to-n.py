#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        def has_zero(x):
            return '0' in str(x)
        count = 0
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                count += 1
        return count # No need for symmetry adjustment because we iterate all pairs (a, b)
# @lc code=end