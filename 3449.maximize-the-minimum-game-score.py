#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
from typing import List
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def can_achieve_min(min_score):
            total_moves = 0
            for point in points:
                if point < min_score:
                    total_moves += min_score - point
            return total_moves <= m
        left, right = 0, max(points) + m + 1
        while left < right:
            mid = (left + right + 1) // 2
            if can_achieve_min(mid):
                left = mid
            else:
                right = mid - 1
        return left
# @lc code=end