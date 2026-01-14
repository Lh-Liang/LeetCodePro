#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            if '0' not in str(a) and '0' not in str(n - a):
                count += 1
        return count
# @lc code=end