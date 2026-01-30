#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def canAchieve(minScore):
            extraMoves = m
            for i in range(len(points)):
                needed = max(0, minScore - points[i])
                if needed > extraMoves:
                    return False
                extraMoves -= needed
            return True
        
        low, high = 0, max(points) + (m // len(points))
        best = low
        while low <= high:
            mid = (low + high) // 2
            if canAchieve(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best # Returns the maximum achievable minimum game score.
# @lc code=end