#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check(x: int) -> bool:
            n = len(points)
            req = [(x + points[i] - 1) // points[i] for i in range(n)]
            if sum(req) > m:
                return False
            vsum = cf = req[n - 1]
            for i in range(n - 2, -1, -1):
                this_f = cf
                v_this = max(req[i], this_f)
                vsum += v_this
                cf = max(0, v_this - this_f)
            extra = max(0, cf - 1)
            return vsum + extra <= m
        left = 0
        right = m * max(points) + 1
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left

# @lc code=end