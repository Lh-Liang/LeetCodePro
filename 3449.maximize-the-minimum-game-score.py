#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def canAchieve(min_score: int) -> bool:
            moves_remaining = m
            for point in points:
                if point < min_score:
                    moves_remaining -= min_score - point
                    if moves_remaining < 0:
                        return False
            return True
        
        low, high = 0, max(points)
        best_min_score = 0
        while low <= high:
            mid = (low + high) // 2
            if canAchieve(mid):
                best_min_score = mid
                low = mid + 1
            else:
                high = mid - 1
        return best_min_score
# @lc code=end